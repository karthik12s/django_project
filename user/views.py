from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, loginForm
def register(request):
    print(request.method)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'user/form.html',{'form':form})

def login(request):
    if(request.method == 'POST'):
        form = loginForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.data)
    else:
        form = loginForm()
    return render(request,'user/login.html',{'form':form})