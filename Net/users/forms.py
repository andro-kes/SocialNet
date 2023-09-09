from django.contrib.auth import forms
from django.contrib.auth.forms import UsernameField 
from django import forms as f
from .models import User

class UserCreationForm(forms.UserCreationForm):
    password1 = f.CharField(
        widget = f.PasswordInput(attrs={
                'class': '',
                'placeholder': 'Придумайте пароль', 
            }
        )
    )
    password2 = f.CharField(
        widget = f.PasswordInput(attrs={
            'class': '',
            'placeholder': 'Повторите пароль',
            }
        )
    )
    
    class Meta:
        model = User
        fields = ['username']
        
        widgets = {
            
        }
        
class AuthForm(forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
    
    username = UsernameField(widget=f.TextInput(attrs={'placeholder': 'Введите имя пользователя',}))
    password = f.CharField(
        widget = f.PasswordInput(attrs={'placeholder': 'Введите пароль',})
    )