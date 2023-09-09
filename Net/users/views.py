from django.shortcuts import render
from django.views import generic as g
from django.contrib.auth import views, login
from .forms import UserCreationForm, AuthForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class MainView(g.View):
    def get(self, request):
        return render(request, 'users/index.html')
   
    
class LoginView(views.LoginView):
    authentication_form = AuthForm
    print('work')


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
            return HttpResponseRedirect(reverse('main'))
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)