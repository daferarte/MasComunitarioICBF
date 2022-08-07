from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import Personas
from grupos.models import Grupos
from asistencia.models import Listas, Horarios, Asistencia
from .forms import RegisterForm
# Create your views here.

def listasdeasistencia(request):
    docente=Personas.objects.filter(user=request.user.id)
    grupos=Grupos.objects.filter(personas__id__in=docente)
    listas=Listas.objects.filter(Grupo__id__in=grupos)
    horarios=Horarios.objects.filter(user=request.user.id).order_by('-create_at')[: 1]
    asistencia=Asistencia.objects.filter(Horario__id__in=horarios, Lista__id__in=listas)
    return render(request, 'asistencia/asistencia.html', {
        'title': 'Home',
        'personas':listas,
        'grupos':grupos,
        'horarios':horarios,
        'asistencia':asistencia
    })

def registroHorario(request):

    #validacion para que redirija si esta registrado el usuario
    if request.user.is_authenticated:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form=RegisterForm(request.POST)

            if(register_form.is_valid()):
                thought = register_form.save(commit=False)
                thought.user = request.user.id
                thought.save()
                #register_form.save()
                messages.success(request,'Registrado Correctamente')
                return redirect('index')

        return render(request, 'asistencia/RegistroHorario.html',{
            'title':'Registro horario',
            'register_form': register_form
        })
        
    else:
        return redirect('index')
        