from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
import pyjokes

from .forms import RegisterForm


# Create your views here.

# def CustomLogin(request):
#   context = {}
#   return render(request, "login/login.html", context)

class SiteLogin(LoginView):
  template_name = 'login/login.html'

def SiteRegister(request):
  form = RegisterForm(request.POST)

  if form.is_valid():
    data = form.cleaned_data

    new_user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password1']
        )
    login(request,user=new_user)
    return redirect('/')
  else:
    context = {'error_list':list(form.error_messages.values())}

    # print(context['error_list'])
    return render(request, "login/register.html", context)
    
    # print(form.error_messages.values())
    # return redirect('login')

def SiteLogout(request):
  logout(request)
  return redirect('/')


# build chat page here
class SiteProfile(LoginRequiredMixin, TemplateView):
  template_name = 'login/login_success.html'

def chatbot_res(request):
  # human_text = request.GET['mess']
  human_text = pyjokes.get_joke()
  return HttpResponse(str(human_text))