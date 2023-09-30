from django.shortcuts import render
from .models import Rooms, Messages

def index(request):
    return render(request, "chats/index.html")

def room(request, room_name):
    if Rooms.objects.filter(name=room_name):
        data = {
            "room_name": room_name,
            'messages': Messages.objects.filter(room_name=room_name)
        }
        return render(request, "chats/room.html", data)
    Rooms.objects.create(name = room_name)
    return render(request, "chats/room.html", {"room_name": room_name})
