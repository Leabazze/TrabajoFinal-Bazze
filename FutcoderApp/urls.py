from django.urls import path,include
from django.contrib.auth.views import LogoutView
from FutcoderApp.views import *
from EquipoApp.views import crear_equipo

urlpatterns = [
    path('', home, name='Home'),
    path('', include ('EquipoApp.urls')),
    path('cancha/', cancha, name='Cancha'),
    path('login/', logear, name='Login'),
    path('registro/', register, name='Registro'),
    path('logout/', LogoutView.as_view(template_name='FutcoderApp/logout.html') , name='Logout'),
    path('prueba/', prueba, name='Prueba'),
    path('intru/', instrucciones, name='Instru'),
    path('opciones', opciones, name='Opciones')
] 