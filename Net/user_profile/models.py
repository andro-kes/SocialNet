from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField('users.User', null=True, on_delete=models.CASCADE)
    ava = models.ImageField(blank=True, null=True, upload_to='images/')
    bio = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.user
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})
