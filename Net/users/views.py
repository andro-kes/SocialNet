from django.shortcuts import render
from django.views import generic as g
from django.contrib.auth import views
from .forms import UserCreationForm

class MainView(g.View):
    def get(self, request):
        return render(request, 'users/index.html')
    
class LoginView(views.LoginView):
    pass

class LogoutView(views.LogoutView):
    pass

class RegisterView(g.View):
    template_name = 'registartion/register.html'
    
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)