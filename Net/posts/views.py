from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Posts
from .forms import CreatePostForm

class CreatePostView(CreateView):
    model = Posts
    template_name = 'posts/create.html'
    form_class = CreatePostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
