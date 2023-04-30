from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import UserCreateForm
from .models import Account

def signupaccount(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            # create user object
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # create account object and associate with user
            Account.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number'],
                birthday=form.cleaned_data['birthday']
            )
            # log in user and redirect to home page
            login(request, user)
            return redirect('home')
    else:
        form = UserCreateForm()
    
    if request.method == 'GET':
        form = UserCreateForm()
        return render(request, 'signupaccount.html', {'form': form})
    else:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                form.add_error('username', 'Username already taken. Choose new username.')
        return render(request, 'signupaccount.html', {'form': form})

@login_required
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html', {'form': AuthenticationForm(), 'error': 'username and password do not match'})
        else:
            login(request,user)
            return redirect('home')
