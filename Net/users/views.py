from django.shortcuts import render
from django.views import generic as g
from django.contrib.auth import views, login
from .forms import UserCreationForm, AuthForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
import json

class MainView(g.View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return render(request, 'users/index.html')
        return HttpResponseRedirect(reverse('register')) 
    
class SearchView(g.list.ListView):
    model = User
    template_name = 'users/search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset'] = json.dumps(list(map(str, list(User.objects.filter().only('username')))))
        return context
    
class LoginView(views.LoginView):
    authentication_form = AuthForm

class LogoutView(views.LogoutView):
    pass


class RegisterView(g.View):
    template_name = 'registration/register.html'
    
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('create_profile'))
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)