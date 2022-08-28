from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Personas, TipoDocumento
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.hashers import make_password
import re
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


@login_required(login_url='login/')
def ActDatosUsu(request):
    usuario = User.objects.get(pk=request.user.id)
    persona= Personas.objects.get(user=usuario)
    tdocumentos = TipoDocumento.objects.all()

    if request.method == 'POST':
        passwd = request.POST.get('password')
        passwd1 = request.POST.get('cnfpassword')
        
        if passwd != passwd1:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('ajustecuenta')
        
        largo = re.compile(r'.{8,}')
        digito = re.compile(r'\d+')
        letra_may = re.compile(r'[A-Z]+')
        letra_min = re.compile(r'[a-z]+')
        simbolo = re.compile(r'[\W.%+-]+')
        
        validaciones = [(largo, "El minimo de la contraseña es de 8 caracteres"),
                (digito, "No tiene digitos"),
                (letra_min, "No tiene letras minúsculas"),
                (letra_may, "No tiene letras mayúsculas"),
                (simbolo, "No tiene simbolos alfanumericos")]
        
        for validacion, mensaje in validaciones:
            if not validacion.search(passwd):
                messages.error(request, f"{passwd}: {mensaje}")
                return redirect('ajustecuenta')
                
        print(passwd)
        if passwd != usuario.password:
            passwd=make_password(passwd, salt=None, hasher='default')

        print(passwd)

        tdocu = request.POST.get('tdocu')
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('firstName')
        apellido = request.POST.get('lastName')
        mail = request.POST.get('email')
        tel = request.POST.get('phoneNumber')
        
        User.objects.filter(pk=request.user.id).update(first_name=nombre, last_name=apellido, email=mail, password=passwd)
        Personas.objects.filter(user=request.user.id).update(tipoDocumento=tdocu,cedula=cedula, telefono=tel)
        
        messages.success(request, 'Datos actualizados con exito')
        return redirect('index')

    return render(request, 'mainapp/actDatosUsu.html', {
        'title': 'Home',
        'usuario':usuario,
        'persona':persona,
        'tdocumentos':tdocumentos,
    })