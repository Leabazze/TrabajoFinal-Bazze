from django.shortcuts import render, redirect
from django.forms import widgets
from .forms import EquipoForm,FifaForm
from .models import *
from random import sample, random, choices, randint, randrange
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
lista_posicion = ['arquero', 'defensor', 'central', 'lat_izq', 'lat_der', 'medio', 'medio_centro','medio_der','medio_izq','enganche','delantero' ]
@login_required
def equipo (req):
    #equipo = Equipo.objects.get(pk=1)
    user = req.user
    equipo = Equipo.objects.get(usuario=user)
    plantel = Plantel.objects.filter(equipo=equipo)

    arquero = plantel.filter(posicion = 'arquero').first()
    defensor = plantel.filter(posicion = 'defensor').first()
    central = plantel.filter(posicion = 'central').first()
    lat_izq = plantel.filter(posicion = 'lat_izq').first()
    lat_der = plantel.filter(posicion = 'lat_der').first()
    medio = plantel.filter(posicion = 'medio').first()
    medio_centro = plantel.filter(posicion = 'medio_centro').first()
    medio_der = plantel.filter(posicion = 'medio_der').first()
    medio_izq = plantel.filter(posicion = 'medio_izq').first()
    enganche = plantel.filter(posicion = 'enganche').first()
    delantero = plantel.filter(posicion = 'delantero').first()
    promedio = calidad_equipo(req)

    lista_posicion = ['arquero', 'defensor', 'central', 'lat_izq', 'lat_der', 'medio', 'medio_centro','medio_der','medio_izq','enganche','delantero' ]

    data = {
        'equipo':equipo,
        'plantel':plantel,
        'arquero':arquero,
        'defensor':defensor,
        'central':central,
        'lat_izq':lat_izq,
        'lat_der':lat_der,
        'medio':medio,
        'medio_centro':medio_centro,
        'medio_izq': medio_izq,
        'medio_der':medio_der,
        'enganche':enganche,
        'delantero':delantero,
        'promedio':promedio,
        'lista_pos':lista_posicion
    }
    return render (req, 'EquipoApp/equipo.html', data)

def calidad_equipo(req):
    user = req.user
    equipo = Equipo.objects.get(usuario=user)
    plantel = Plantel.objects.filter(equipo=equipo)
    jugadores = plantel.all()
    puntaje = 0
    for i in jugadores:
        puntaje += int(i.general)
    promedio = puntaje // 11
    #cuantos = len(plantel)
    return promedio

def ver_jugadores(req):
    global posicion
    posicion = req.POST.get('posicion')
    if posicion == 'arquero':
        jugadores = Fifa.objects.filter(reflexes__range =(70,99)).order_by('-gen')
    elif posicion =='defensor':
        jugadores = Fifa.objects.filter(consciencedefensive__gte =75, tacledebout__gte = 75 ).order_by('-gen')
    elif posicion == 'central':
        jugadores = Fifa.objects.filter(consciencedefensive__gte =75, tacledebout__gte = 75 ).order_by('-gen')
    elif posicion == 'lat_izq':
        jugadores = Fifa.objects.filter(consciencedefensive__gte =70, vitesse__gte = 80 ).order_by('-gen')
    elif posicion == 'lat_der':
        jugadores = Fifa.objects.filter(consciencedefensive__gte =70, vitesse__gte = 80 ).order_by('-gen')
    elif posicion == 'medio':
        jugadores = Fifa.objects.filter(consciencedefensive__gte =70, vitesse__gte = 75, vista__gte =75 ).order_by('-gen')
    elif posicion == 'medio_centro':
        jugadores = Fifa.objects.filter(consciencedefensive__gte =70, vitesse__gte = 75, interceptions__gte=75, tacledebout__gte = 75 ).order_by('-gen')
    elif posicion == 'medio_der':
        jugadores = Fifa.objects.filter(vitesse__gte =70, agilite__gte =75 ).order_by('-gen')
    elif posicion == 'medio_izq':
        jugadores = Fifa.objects.filter(vitesse__gte =70, agilite__gte =75 ).order_by('-gen')
    elif posicion == 'enganche':
        jugadores = Fifa.objects.filter(vista__gte =70, vitesse__gte = 75,agilite__gte =75, passeslongues__gte = 75,passescourtes__gte = 80 ).order_by('-gen')
    elif posicion == 'delantero':
        jugadores = Fifa.objects.filter(vitesse__gte = 75, pcf__gte = 78, finition__gte = 80).order_by('-gen')
    data = {
        'jugadores':jugadores,
        'posicion':posicion
        }
    context = data
    return render (req, 'EquipoApp/jugadores.html', context )



@login_required
def comprar_jugador(req, id):
    if req.method == 'POST':
        user = req.user
        equipo = Equipo.objects.get(usuario=user)
        jugador = Fifa.objects.get(id=id)
        costo= int(jugador.valeur)  
        #equipo = Equipo.objects.get(pk=1)
        user = req.user
        equipo = Equipo.objects.get(usuario=user)
        presupuesto = (equipo.presupuesto)
        if costo <= presupuesto:
            equipo.presupuesto -= costo
            equipo.save(update_fields=['presupuesto'])
            presupuesto_nuevo = equipo.presupuesto
            jugador_comprado = Plantel(
                usuario = user,
                jugador=jugador,
                nombre=jugador.nom,
                valor=jugador.valeur,
                general=jugador.gen,
                pais=jugador.pays,
                posicion=posicion,
                equipo=equipo
                        )
            jugador_comprado.save()
            equipo.save()
            data = {
                'jugador_comprado':jugador_comprado,
                'presupuesto':presupuesto_nuevo,
                'mensaje': f'compra exitosa'
            }
            return render (req, 'EquipoApp/comprar-jugador.html', data)
        return render(req, 'EquipoApp/comprar-jugador.html',{'mensaje':f'no te alcanza el presupuesto'})
    else:
        return render (req, 'EquipoApp/equipo.html')
    
@login_required
def vender(req, id):
    if req.method == 'POST':
        jugador = Plantel.objects.get(id=id)
        #equipo = Equipo.objects.get(id=1)
        user = req.user
        equipo = Equipo.objects.get(usuario=user)
        equipo.presupuesto += jugador.valor
        equipo.save(update_fields=['presupuesto'])
        jugador.delete()
        return redirect ('Equipo')
    
def buscar_nombre(req):
    if req.GET['nom']:
        general = req.GET['nom']
        jugadores = Fifa.objects.filter(nom__icontains=general)

        data = {
            'jugadores':jugadores
        }
        return render (req , 'EquipoApp/buscar-nombre.html', data)

def buscar_precio(req):
    if req.GET['valeur']:
        precio = req.GET['valeur']
        jugadores = Fifa.objects.filter(valeur__gte=precio).order_by('valeur')[:50]
        #paginator = Paginator(jugadores, 15)
        
        #pagina = req.GET.get('page',1)# requiere un numero de pagina en su defecto es la uno
        #jugadores= paginator.page(pagina)
    
        data = {
            'jugadores':jugadores,
            }
        return render(req, 'EquipoApp/buscar-precio.html',data)

@login_required 
def crear_equipo(req):
    if req.method == 'POST':
        miFormulario = EquipoForm(req.POST)
        user = req.user
        anterior_equipo = Equipo.objects.filter(usuario=user).first()
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            equipo = Equipo(nombre=data['nombre'], usuario=user)
            equipo.save()

            if anterior_equipo:
                anterior_equipo.delete()
        return render (req, 'EquipoApp/equipo.html', {'equipo':equipo})
    else :
        miFormulario = EquipoForm()
        return render (req, 'EquipoApp/crear-equipo.html',{'miFormulario':miFormulario})
    

def guardar_fifa(req):
    if req.method == 'POST':
        miFormulario = FifaForm(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            jugador = Fifa(nom=data['nom'], club=data['club'])
            jugador.save()
        return render (req, 'EquipoApp/fifa.html')
    else :
        miFormulario = FifaForm()
        return render (req, 'EquipoApp/fifa.html',{'miFormulario':miFormulario})
    
#funcion que utilice para guardar los clubes desde la base de datos fifa, la cual tiene un error por que 
#guardo por cada jugador un club, luego borre los registros repetidos desde el db browser
def rivales(req):
    clubes = Fifa.objects.values_list('club', flat=True).distinct()
    clubes_data = []
    for club in clubes:
        jugadores = Fifa.objects.filter(club__contains=club)
        suma_gen = 0
        for jugador in jugadores:
            suma_gen += int(jugador.gen)
        cant_jugadores = jugadores.count()
        promedio = suma_gen / cant_jugadores
        if promedio >= 56 and promedio <= 65:
            club_guardar = Clubes(nombre=club, general=promedio, categoria="D")
            club_guardar.save()
            clubes_data.append({
                'club':club,
                'promedio': promedio,
            })
    data ={
        'clubes':clubes_data
    }
    return render(req, 'EquipoApp/clubes.html',data )


@login_required
def categorias(req):
    user = req.user
    equipo = Equipo.objects.get(usuario=user)
    categoria_a = equipo.categoria
    clubes_a = Clubes.objects.filter(categoria=categoria_a)
    clubes_lista = []
    #equipos_creados = Torneo.objects.filter(cat=categoria_a).count()
    #if equipos_creados == 10:
    #    return render
    #else:
    for club in clubes_a:
        clubes_lista.append(club)
    clubes_final = random.sample(clubes_lista, 10)
    for club in clubes_final:
        club_db = Torneo(
            cat=club.categoria,
            nombre=club.nombre,
            gen=club.general,
            usuario = user
        )
        club_db.save()

        
    data = {
        'clubes': clubes_final
    }
    return render(req, 'EquipoApp/categorias.html', data)

@login_required
def borrar_categorias(req):
    user = req.user
    equipo = Equipo.objects.get(usuario=user)
    categoria_a = equipo.categoria
    clubes_a = Torneo.objects.filter(cat=categoria_a)
    clubes_a.delete()
    return render(req,'FutcoderApp/cancha.html')



def simular (req):
    user = req.user
    equipo = Equipo.objects.get(usuario=user)
    categoria_db = equipo.categoria
    torneo_db = Torneo.objects.filter(cat = categoria_db)
    jugado = Puntos.objects.filter(categoria=categoria_db).values_list('club__nombre', flat=True)
    puntos = Puntos.objects.filter(categoria=categoria_db).values_list('puntos_db', flat=True)
    resultados = Puntos.objects.filter(categoria=categoria_db).filter(resultado_mio__isnull=False).filter(resultado_rival__isnull=False)
    partidos= len(jugado)
    puntos_totales=0
    for p in puntos:
        puntos_totales += p
    #    todos = Puntos.objects.all()
    promedio = calidad_equipo(req)
    #resultados = Puntos.objects.filter(categoria=categoria_db).filter(resultado_mio__isnull=False).filter(resultado_rival__isnull=False)
    data = {
        'torneo':torneo_db,
        'jugado':jugado,
        'puntos':puntos_totales,
        'partidos':partidos,
        'promedio': promedio,
        'resultados':resultados,
        'categoria':categoria_db,
        'equipo':equipo
        }
    if req.method == 'POST':
        borrar_resultados(req)
        return redirect('Simular')
    return render (req, 'EquipoApp/simular.html',data)

def borrar_resultados(req):
    Puntos.objects.all().delete()
    return redirect('Simular')

def jugar (req):
    if req.method == 'POST':
        user = req.user
        equipo = Equipo.objects.get(usuario=user)
        plantel = Plantel.objects.filter(equipo=equipo)
        cant_plantel = plantel.count()
    
        puntos = 0
        nombre_rival =req.POST['rival']
        global lista_jugados
        lista_jugados = []
        clubes_db = Torneo.objects.get(nombre=nombre_rival)
        lista_jugados.append(clubes_db)
        rival_gen = clubes_db.gen
        if rival_gen >= 80:
            resultado_rival = randrange(2,8)
        elif rival_gen < 80 and rival_gen >= 77:
            resultado_rival = randrange(1,7)
        elif rival_gen < 77 and rival_gen >=75:
            resultado_rival = randrange(0,7)
        elif rival_gen < 75 and rival_gen >=70:
            resultado_rival = randrange(1,6)
        elif rival_gen < 70 and rival_gen >=65:
            resultado_rival = randrange(0,5)
        elif rival_gen < 65 and rival_gen >=60:
            resultado_rival = randrange(0,4)
        else:
            resultado_rival = randrange(0,3)
        promedio = calidad_equipo(req)
        if promedio >= 83:
            resultado_mio = randrange(3,7)
        elif promedio > 80 and promedio <=82: 
            resultado_mio = randrange(2,7)
        elif promedio >75 and promedio <=80:
            resultado_mio = randrange(1,7)
        elif promedio >70 and promedio <=75:
            resultado_mio = randrange(0,6)
        elif promedio >65 and promedio <=70:
            resultado_mio = randrange(0,5)
        elif promedio >60 and promedio <=65:
            resultado_mio = randrange(2,4)
        elif promedio >40 and promedio <=60:
            resultado_mio = randrange(0,3)
        else:
            return render (req, 'EquipoApp/jugar.html',{'mensaje':f'no puedes jugar con un promedio general menor de 40 y el tuyo es: {promedio}'})
        messi = plantel.filter(nombre__contains="Messi")
        if messi:
            resultado_mio += 1
            saber='messi esta'
        saber='no'
        if resultado_mio > resultado_rival:
            resultado = 'GANASTE'
            puntos = puntos + 3
        elif resultado_mio == resultado_rival:
            resultado = 'EMPATE'
            puntos +=1
        else:
            resultado= 'PERDISTE'
        juego = Puntos(
            usuario = user,
            club = clubes_db,
            nombre = nombre_rival,
            puntos_db = puntos,
            categoria = clubes_db.cat,
            resultado_rival = resultado_rival,
            resultado_mio = resultado_mio
        )
        juego.save()
        data = {
            'resultado': resultado,
            'resultado_mio': resultado_mio,
            'resultado_rival': resultado_rival,
            'nombre': nombre_rival,
            'lista':lista_jugados,
            'cantidad':cant_plantel,
            'saber':saber,
            'equipo':equipo
        }

        return render (req, 'EquipoApp/jugar.html', data)
    
@login_required
def ascender (req):
    puntos = Puntos.objects.values_list('puntos_db', flat=True)
    puntos_totales = sum(puntos)
    categorias_t = ['E', 'D', 'C', 'B','A']
    if puntos_totales >= 20:
        user = req.user
        equipo = Equipo.objects.get(usuario=user)
        categoria_actual = equipo.categoria
        indice_actual = categorias_t.index(categoria_actual)
        if categoria_actual != 'A':
            equipo.presupuesto += 50000000
            equipo.save(update_fields=['presupuesto'])
            nueva_categoria = categorias_t[indice_actual +1]
            equipo.categoria = nueva_categoria
            equipo.save(update_fields=['categoria'])
            data = {
                'presupuesto': equipo.presupuesto,
                'categoria': nueva_categoria
            }
            return render (req, 'EquipoApp/categorias.html', data)
        else:
            return render(req, 'EquipoApp/campeon.html')