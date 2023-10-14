from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile
from posts.models import Posts
from .forms import CreateProfileForm

class ProfileView(DetailView):
    model = Profile
    template_name = 'user_profile/profile.html'
    context_object_name = 'profile'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Posts.objects.filter(author=self.request.user)
        return context

class CreateProfileView(CreateView):
    model = Profile 
    template_name = 'user_profile/create.html'
    form_class = CreateProfileForm
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'user_profile/create.html'
    form_class = CreateProfileForm
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = Profile.objects.get(user=self.request.user)
        context['ava_preview'] = user.ava
        context['title_update'] = 'Редактирование профиля'
        return context
    
