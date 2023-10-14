from django.forms import ModelForm
from django import forms
from .models import Posts

class CreatePostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['comment', 'image']
        
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'forms',
                'placeholder': 'Комментарий',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'image-form',
                'id': 'image_form',
            }),
        }