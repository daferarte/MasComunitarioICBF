from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from grupos.models import Grupos
from asistencia.models import Listas, Horarios, Asistencia
from .forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login/')
def listasdeasistencia(request):
    docente = User.objects.filter(pk=request.user.id)[: 1]
    grupos = Grupos.objects.filter(usuario__id__in=docente)
    listas = Listas.objects.filter(Grupo__id__in=grupos)
    horarios = Horarios.objects.filter(user__id__in=docente).order_by('-create_at')[: 1]
    try:
        idh = Horarios.objects.get(pk=horarios)
    except Horarios.DoesNotExist:
        idh = 'Aún no se ha creado un encuentro'

    asistentes = Asistencia.objects.filter(Horario__id__in=horarios, Lista__id__in=listas)

    if request.method == 'POST':
        for i in listas:
            #  Horario = int(request.POST.get('idh'+str(i.id)))
            if (request.POST.get('estado' + str(i.id)) is None):
                asiste = False
            else:
                asiste = True

            asistencia = Asistencia(
                Horario=idh,
                Lista=i,
                asiste=asiste
            )
            asistencia.save()
        messages.success(request, 'Registrado Correctamente')
        return redirect('Asistencia')

    return render(request, 'asistencia/asistencia.html', {
        'title': 'Home',
        'personas': listas,
        'grupos': grupos,
        'horarios': idh,
        'asistencia': asistentes
    })


@login_required(login_url='login/')
def VerHorarios(request):
    
    docente = User.objects.filter(pk=request.user.id)[: 1]
    horarios = Horarios.objects.filter(user__id__in=docente).order_by('-create_at')

    return render(request, 'asistencia/ListaHorarios.html', {
        'title': 'Home',
        'horarios': horarios,
    })


@login_required(login_url='login/')
def ActListasAsistencia(request, horario_id):
    
    docente = User.objects.filter(pk=request.user.id)[: 1]
    grupos = Grupos.objects.filter(usuario__id__in=docente)
    listas = Listas.objects.filter(Grupo__id__in=grupos)
    horario = get_object_or_404(Horarios, id=horario_id)
    asistentes = Asistencia.objects.filter(Horario=horario, Lista__id__in=listas)
    
    if request.method == 'POST':
        for i in listas:
            #  Horario = int(request.POST.get('idh'+str(i.id)))
            if (request.POST.get('estado' + str(i.id)) is None):
                asiste = False
            else:
                asiste = True
            
            asistentes = Asistencia.objects.filter(Horario=horario, Lista=i).update(asiste = asiste)
            
        messages.success(request, 'Registrado Correctamente')
        return redirect('ActAsistencia', horario_id)

    return render(request, 'asistencia/actasistencia.html', {
        'title': 'Home',
        'horarios': horario,
        'personas': asistentes
    })


@login_required(login_url='login/')
def guardarDatos(request):
    dat = ['24339612', '1061748566', '34513190', '36758469', '1130642292', '37083399', '1083891603', '87067539', '1081404295', '1085920621', '1085262669', '1085320329', '1085264688', '1085246466', '36954621', '1122783881', '1085325986', '87061246', '1085305227', '1085293619', '1085250401', '1061792534', '1088596087', '37087810', '59312852', '89008319', '41956052', '1053824875', '1049631763', '37686899', '1098604701', '63547507', '37275197', '63557032', '34502171', '31710168', '1015411874', '1130639294', '34772019', '43602806', '38602485', '1004545915', '113665182', '1096033717', '22793738', '16727719', '31320533', '1085280569', '1143935912', '1083894795', '38560373']
    for i in dat:
        user = User(
            username=str(i),
            password=make_password('Cesm123$', salt=None, hasher='default')
        )
        #  print(user.password)
        user.save()


@login_required(login_url='login/')
def registroHorario(request):

    #  validacion para que redirija si esta registrado el usuario
    if request.user.is_authenticated:
        register_form = RegisterForm()
        docente = request.user.username
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if (register_form.is_valid()):
                thought = register_form.save(commit=False)
                thought.user = request.user
                thought.save()
                #  register_form.save()
                messages.success(request, 'Registrado Correctamente')
                return redirect('index')

        return render(request, 'asistencia/RegistroHorario.html', {
            'title': 'Registro horario',
            'register_form': register_form,
            'usuario': docente
        })
    else:
        return redirect('index')
