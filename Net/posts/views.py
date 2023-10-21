from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Posts
from .forms import CreatePostForm
from django.views.generic.detail import DetailView

class CreatePostView(CreateView):
    model = Posts
    template_name = 'posts/create.html'
    form_class = CreatePostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class DetailPostView(DetailView):
    model = Posts
    template_name = 'posts/detail.html'
    context_object_name = 'post'
        
