from django import forms
from .models import Profile

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['ava', 'name', 'surname', 'status', 'bio', 'slug']
        
        widgets = {
            'ava': forms.ClearableFileInput(attrs={
                'class': 'ava-link',
                'label': None,
                'id': 'ava_id',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите имя',
                'class': 'forms base_form',
            }),
            'surname': forms.TextInput(attrs={
                'placeholder': 'Введите фамилию',
                'class': 'forms base_form',
            }),
            'status': forms.TextInput(attrs={
                'placeholder': 'Установите статус',
                'class': 'forms base_form',
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Расскажите о себе',
                'class': 'forms bio_form',
            }),
            'slug': forms.TextInput(attrs={
                'hidden': True,
                'id': 'slug_field',
            }),
        }
        
        