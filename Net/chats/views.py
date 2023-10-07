from django.shortcuts import render
from .models import Rooms, Messages
from user_profile.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    user = request.user.username
    friends={}
    active_rooms = Rooms.objects.filter(name__contains=user)
    active_rooms = filter(lambda room_name: user == str(room_name).split('_')[0] or user == str(room_name).split('_')[1], active_rooms)
    for room in active_rooms:
        users = str(room.name).split('_')
        if users[0] != user:
            friend = User.objects.get(username=users[0])
            friends[str(room.name)] = Profile.objects.get(user=friend.id)
        else:
            friend = User.objects.get(username=users[1])
            friends[str(room.name)] = Profile.objects.get(user=friend.id)
    data = {
        'active_rooms': friends,
    }
    return render(request, "chats/index.html", data)

def room(request, room_name):
    for n in room_name.split('_'):
        if n != request.user.username:
            friend_username = User.objects.get(username=n)
            friend = Profile.objects.get(user=friend_username.id)
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
