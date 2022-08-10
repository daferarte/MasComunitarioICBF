from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from mainapp.models import Personas
from grupos.models import Grupos
from asistencia.models import Listas, Horarios, Asistencia
from .forms import RegisterForm
# Create your views here.

def listasdeasistencia(request):
    docente=Personas.objects.filter(user=request.user.id)[: 1]
    grupos=Grupos.objects.filter(personas__id__in=docente)
    listas=Listas.objects.filter(Grupo__id__in=grupos)
    horarios=Horarios.objects.filter(personas__id__in=docente).order_by('-create_at')[: 1]
    try:
        idh=get_object_or_404(Horarios,pk=horarios)
    except:
        idh='Aun no se a creado un horario'
        
    asistencia=Asistencia.objects.filter(Horario__id__in=horarios, Lista__id__in=listas)
    if request.method == 'POST':
        for i in listas:            
            #Horario = int(request.POST.get('idh'+str(i.id)))
            Lista = int(i.id)
            if (request.POST.get('estado'+str(i.id)) is None) : 
                asiste = False
            else:
                asiste = True 
            print(idh)
            print(Lista)
            print(asiste)

            asistencia=Asistencia(
                Horario=idh,
                Lista=i,
                asiste=asiste
                
            )
            asistencia.save()
            messages.success(request,'Registrado Correctamente')
            return redirect('index')

    return render(request, 'asistencia/asistencia.html', {
        'title': 'Home',
        'personas':listas,
        'grupos':grupos,
        'horarios':idh,
        'asistencia':asistencia
    })

def registroHorario(request):

    #validacion para que redirija si esta registrado el usuario
    if request.user.is_authenticated:
        register_form = RegisterForm()
        docente=Personas.objects.get(pk=request.user.id)
        if request.method == 'POST':
            register_form=RegisterForm(request.POST)

            if(register_form.is_valid()):
                thought = register_form.save(commit=False)
                thought.personas = docente
                thought.save()
                #register_form.save()
                messages.success(request,'Registrado Correctamente')
                return redirect('index')

        return render(request, 'asistencia/RegistroHorario.html',{
            'title':'Registro horario',
            'register_form': register_form,
            'usuario':docente
        })
        
    else:
        return redirect('index')
        