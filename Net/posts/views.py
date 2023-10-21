from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Posts
from chats.models import Comments
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(post_id=kwargs['object'])
        return context
        
