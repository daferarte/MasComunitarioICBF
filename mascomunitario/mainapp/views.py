from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


@login_required(login_url='login/')
def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Home',
    })


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if (user is not None):
                login(request, user)

                return redirect('index')
            else:
                messages.warning(request, 'Usuario o contraseña incorrectos')
        return render(request, 'mainapp/login.html', {
            'title': 'Identificate',
        })


def logout_user(request):
    logout(request)
    return redirect('login')
