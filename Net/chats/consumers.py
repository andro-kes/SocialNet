import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Messages, Comments
from posts.models import Posts
from django.contrib.auth import get_user_model

User = get_user_model()

def getUserName(username):
    return User.objects.get(username__exact=username)

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]
        Messages.objects.create(
            user=getUserName(user),
            room_name=self.room_name,
            text=message
        )
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, 'user': user}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        user = event['user']
        self.send(text_data=json.dumps({"message": message, 'user': user}))   
    
        
class CommentConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json['user']
        time = text_data_json['time']
        post_id = text_data_json['post_id']
        Comments.objects.create(
            post_id=Posts.objects.get(id=int(post_id)),
            author=User.objects.get(username=user),
            text=message
        )
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, 'post_id': post_id, 'user': user, 'time': time}
        )
    def chat_message(self, event):
        message = event["message"]
        user = event['user']
        time = event['time']
        post_id = event['post_id']
        self.send(text_data=json.dumps({"message": message, 'user': user, 'time': time, 'post_id': post_id}))  