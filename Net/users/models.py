from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    
    def get_absolute_url(self):
        return reverse('main')
    
class Friends(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='sent')
    friend = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='receive')
    
    def __str__(self):
        return str(self.user)+str(self.friend)
    
