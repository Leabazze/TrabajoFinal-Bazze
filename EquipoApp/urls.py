from django.urls import path
from EquipoApp.views import *
from django.urls import path,include
from FutcoderApp.views import *

urlpatterns = [
    path('equipo/', equipo, name= 'Equipo'),
    path('jugadores/', ver_jugadores, name= 'Jugadores'),
    path('comprar-jugador/<int:id>', comprar_jugador, name= 'ComprarJugador'),
    path('vender/<int:id>', vender, name= 'Vender'),
    path('buscar-nombre/', buscar_nombre, name='BuscarNombre'),
    path('buscar-precio/', buscar_precio, name='BuscarPrecio'),
    path('crear-equipo/',crear_equipo, name='CrearEquipo'),
    path('puntaje/', calidad_equipo, name='Puntaje'),
    path('fifa/', guardar_fifa, name='Fifa'),
    path('clubes/', rivales, name='Clubes'),
    path('categorias/', categorias , name='Categorias'),
    path('jugar/', jugar, name='Jugar'),
    path('simular/', simular, name='Simular'),
    path('ascender/', ascender, name='Ascender'),
    path('borrar/', borrar_resultados, name='BorrarResultados'),
    path('borrar-cat/', borrar_categorias, name='BorrarCat'),
]   