from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignUpForm
from django.contrib.auth import login, logout

def signin(request):
  form = UserLoginForm()

  if request.method == 'POST':
    form = UserLoginForm(request, request.POST)

    if form.is_valid():
      login(request, form.get_user())
      return redirect('main:index')

  return render(request, 'signin.html', {'form': form})


def signup(request):

  form = UserSignUpForm()

  if request.method == 'POST':
    form = UserSignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('main:index')
    
  return render(request, 'signup.html', {'form': form})


def signout(request):
  logout(request)
  return redirect('main:index')