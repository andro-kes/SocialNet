from django.shortcuts import render
from .models import Rooms, Messages
from user_profile.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    return render(request, "chats/index.html")

def room(request, room_name):
    for n in room_name.split('_'):
        if n != request.user.username:
            friend_username = User.objects.get(username__exact=n)
            friend = Profile.objects.get(user__exact=friend_username.id)
            break
    if Rooms.objects.filter(name=room_name):
        data = {
            "room_name": room_name,
            'messages': Messages.objects.filter(room_name=room_name),
            'friend_name': friend,
        }
        return render(request, "chats/room.html", data)
    Rooms.objects.create(name = room_name)
    data = {
        'room_name': room_name,
        'friend_name': friend,
    }
    return render(request, "chats/room.html", data)
