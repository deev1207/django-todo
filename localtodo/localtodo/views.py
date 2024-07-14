from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def index(request):
    return redirect('/todo')
def SignUpView(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/todo/')
        
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})   