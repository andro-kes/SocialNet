from django.db import models

class Rooms(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Messages(models.Model):
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)
    room_name = models.CharField(max_length=255)
    text = models.TextField()
    data = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
