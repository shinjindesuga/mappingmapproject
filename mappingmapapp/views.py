from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import MapModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'

def signupfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    try:
      User.objects.get(username=username)
      return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
    except:
      user = User.objects.create_user(username, '', password)
      return redirect('login')
  return render(request, 'signup.html', {'some':100})

def loginfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('list')
    else:
      return render(request, 'login.html', {'error':'ユーザーが存在しません'})
  else:
    return render(request, 'login.html')

class MapList(ListView):
  template_name = 'maplist.html'
  model = MapModel

def logoutfunc(request):
  logout(request)
  return redirect('login')

class MapDetail(DetailView):
  template_name = 'detail.html'
  model = MapModel

class MapCreate(LoginRequiredMixin, CreateView):
  template_name = 'create.html'
  model = MapModel
  fields = ('title','content', 'image')
  success_url = reverse_lazy('list')