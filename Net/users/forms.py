from django.contrib.auth import forms
from django.contrib.auth.forms import UsernameField 
from django import forms as f
from .models import User

class UserCreationForm(forms.UserCreationForm):
    password1 = f.CharField(
        widget = f.PasswordInput(attrs={
                'class': 'forms',
                'placeholder': 'Придумайте пароль', 
            }
        )
    )
    password2 = f.CharField(
        widget = f.PasswordInput(attrs={
            'class': 'forms',
            'placeholder': 'Повторите пароль',
            }
        )
    )
    
    class Meta:
        model = User
        fields = ['username']
        
        widgets = {
            'username': f.TextInput(attrs={
                'class': 'forms', 
                'placeholder': 'Введите имя пользвоателя',
            })
        }
        
class AuthForm(forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
    
    username = UsernameField(widget=f.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
        'class': 'forms',
        }))
    password = f.CharField(
        widget = f.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
            'class': 'forms',
        })
    )
    
class SearchForm(f.Form):
    name = f.CharField(
        widget = f.TextInput(attrs={
            'hidden': True,
        })
    )