from EquipoApp.models import Fifa, Clubes

def rivales(req):
    clubes = Fifa.objects.values_list('club', flat=True)
    for club in clubes:
        jugadores = Fifa.objects.filter(club__contains=club)
        suma_gen = 0
        for jugador in jugadores:
            suma_gen += int(jugador.gen)
        cant_jugadores = jugadores.count()
        promedio = suma_gen / cant_jugadores

        club_cargar = Clubes(nombre = club.club, general = promedio)
        club_cargar.save()
