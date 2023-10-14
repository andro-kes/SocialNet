from django.db import models
from django.urls import reverse

class Posts(models.Model):
    author = models.ForeignKey('users.User', null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='posts/')
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author)
    
    def get_absolute_url(self):
        return reverse("main")
    
