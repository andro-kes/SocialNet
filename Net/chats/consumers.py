import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Messages
from django.contrib.auth import get_user_model

User = get_user_model()

def getUserName(username):
    return User.objects.get(username__iexact=username)

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