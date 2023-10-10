from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from EquipoApp.models import Plantel,Equipo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def home (req):

    return render (req, 'FutcoderApp/home.html') # en realidad hace referencia al lugar del archivo 

def opciones(req):
    return render (req, 'FutcoderApp/opciones.html')

#def equipo (req):

    return render (req, 'FutcoderApp//equipo.html')
@login_required
def cancha (req):
    user = req.user
    try:
        equipo = Equipo.objects.get(usuario=user)
        lista = Plantel.objects.filter(equipo=equipo)
        data = {
            'lista':lista,
            'usuario':user
        }
        return render (req, 'FutcoderApp/cancha.html', data)
    except Equipo.DoesNotExist:
        return redirect('CrearEquipo')


def instrucciones(req):
    return render(req, 'FutcoderApp/instru.html')

@login_required
def prueba (req):
    user = req.user
    equipo = Equipo.objects.get(usuario=user)
    lista = Plantel.objects.filter(equipo=equipo)
    data = {
        'lista':lista,
        'mensaje':f'probando'
    }
    return render (req, 'FutcoderApp/prueba.html', data)

def logear (req):
    if req.method =='POST':
        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            usuario = data['username']
            psw = data['password'] 
            # con user guardamos lo que nos de el metodo authenticate, si no existe da none
            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render (req, 'FutcoderApp/home.html', {'mensaje': f'bienvenido {usuario}'})
        return render (req, 'FutcoderApp/home.html', {'mensaje': f'datos incorrectos'})
    else:
        miFormulario=AuthenticationForm()
        return render (req, 'FutcoderApp/login.html', {'miFormulario': miFormulario})

def register(req):
    if req.method =='POST':
        miFormulario = UserCreationForm(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data['username']
            miFormulario.save()
            
            return render (req, 'FutcoderApp/home.html', {'mensaje': f'usuario: {usuario} craedo con exito!'})
        
        return render (req, 'FutcoderApp/home.html', {'mensaje': f'formulario invalido!'})

    else:
        miFormulario=UserCreationForm()
        return render (req, 'FutcoderApp/registro.html', {'miFormulario': miFormulario})