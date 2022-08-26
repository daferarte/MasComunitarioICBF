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
        idh = Horarios.objects.filter(pk=horarios)
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
        return redirect('index')

    return render(request, 'asistencia/asistencia.html', {
        'title': 'Home',
        'personas': listas,
        'grupos': grupos,
        'horarios': idh,
        'asistencia': asistentes
    })


@login_required(login_url='login/')
def guardarDatos(request):
    dat = ['16727719', '22793738', '24339612', '31320533', '31710168', '34502171', '34513190', '34772019', '36758469', '36954621', '37083399', '37087810', '37275197', '37686899', '38560373', '38602485', '41956052', '43602806', '59312852', '63547507', '63557032', '87061246', '87067539', '89008319', '113665182', '1004545915', '1015411874', '1049631763', '1053824875', '1061748566', '1061792534', '1081404295', '1083891603', '1083894795', '1085246466', '1085250401', '1085262669', '1085264688', '1085280569', '1085293619', '1085305227', '1085320329', '1085325986', '1085920621', '1088596087', '1096033717', '1098604701', '1122783881', '1130639294', '1130642292', '1143935912']
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
