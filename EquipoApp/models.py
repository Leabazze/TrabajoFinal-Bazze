from django.db import models, transaction
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Fifa(models.Model):
        nom = models.TextField(db_column='Nom', blank=True, null=True)  # Field name made lowercase.
        gen = models.IntegerField(db_column='Gen', blank=True, null=True)  # Field name made lowercase.
        potentiel = models.IntegerField(db_column='Potentiel', blank=True, null=True)  # Field name made lowercase.
        performance = models.FloatField(db_column='Performance', blank=True, null=True)  # Field name made lowercase.
        pays = models.TextField(db_column='Pays', blank=True, null=True)  # Field name made lowercase.
        club = models.TextField(db_column='Club', blank=True, null=True)  # Field name made lowercase.
        bonpied = models.TextField(db_column='Bonpied', blank=True, null=True)  # Field name made lowercase.
        mauvaispied = models.IntegerField(db_column='Mauvaispied', blank=True, null=True)  # Field name made lowercase.
        gestestechniques = models.IntegerField(db_column='Gestestechniques', blank=True, null=True)  # Field name made lowercase.
        taille = models.IntegerField(db_column='Taille', blank=True, null=True)  # Field name made lowercase.
        rendementoffensif = models.TextField(db_column='Rendementoffensif', blank=True, null=True)  # Field name made lowercase.
        rendementdefensif = models.TextField(db_column='Rendementdefensif', blank=True, null=True)  # Field name made lowercase.
        valeur = models.IntegerField(db_column='Valeur', blank=True, null=True)  # Field name made lowercase.
        salaire = models.TextField(db_column='Salaire', blank=True, null=True)  # Field name made lowercase.
        id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
        centres = models.IntegerField(db_column='Centres', blank=True, null=True)  # Field name made lowercase.
        finition = models.IntegerField(db_column='Finition', blank=True, null=True)  # Field name made lowercase.
        precisiontete = models.IntegerField(db_column='Precisiontete', blank=True, null=True)  # Field name made lowercase.
        passescourtes = models.IntegerField(db_column='Passescourtes', blank=True, null=True)  # Field name made lowercase.
        volee = models.IntegerField(db_column='Volee', blank=True, null=True)  # Field name made lowercase.
        dribbles = models.IntegerField(db_column='Dribbles', blank=True, null=True)  # Field name made lowercase.
        effet = models.IntegerField(db_column='Effet', blank=True, null=True)  # Field name made lowercase.
        pcf = models.IntegerField(db_column='PCF', blank=True, null=True)  # Field name made lowercase.
        passeslongues = models.IntegerField(db_column='Passeslongues', blank=True, null=True)  # Field name made lowercase.
        controle = models.IntegerField(db_column='Controle', blank=True, null=True)  # Field name made lowercase.
        acceleration = models.IntegerField(db_column='Acceleration', blank=True, null=True)  # Field name made lowercase.
        vitesse = models.IntegerField(db_column='Vitesse', blank=True, null=True)  # Field name made lowercase.
        agilite = models.IntegerField(db_column='Agilite', blank=True, null=True)  # Field name made lowercase.
        reactivite = models.IntegerField(db_column='Reactivite', blank=True, null=True)  # Field name made lowercase.
        equilibre = models.IntegerField(db_column='Equilibre', blank=True, null=True)  # Field name made lowercase.
        puissancefrappe = models.IntegerField(db_column='Puissancefrappe', blank=True, null=True)  # Field name made lowercase.
        detente = models.IntegerField(db_column='Detente', blank=True, null=True)  # Field name made lowercase.
        endurance = models.IntegerField(db_column='Endurance', blank=True, null=True)  # Field name made lowercase.
        force = models.IntegerField(db_column='Force', blank=True, null=True)  # Field name made lowercase.
        tirsdeloin = models.IntegerField(db_column='Tirsdeloin', blank=True, null=True)  # Field name made lowercase.
        agressivite = models.IntegerField(db_column='Agressivite', blank=True, null=True)  # Field name made lowercase.
        interceptions = models.IntegerField(db_column='Interceptions', blank=True, null=True)  # Field name made lowercase.
        placement = models.IntegerField(db_column='Placement', blank=True, null=True)  # Field name made lowercase.
        vista = models.IntegerField(db_column='Vista', blank=True, null=True)  # Field name made lowercase.
        penalty = models.IntegerField(db_column='Penalty', blank=True, null=True)  # Field name made lowercase.
        calme = models.IntegerField(db_column='Calme', blank=True, null=True)  # Field name made lowercase.
        consciencedefensive = models.IntegerField(db_column='Consciencedefensive', blank=True, null=True)  # Field name made lowercase.
        tacledebout = models.IntegerField(db_column='Tacledebout', blank=True, null=True)  # Field name made lowercase.
        tacleglisse = models.IntegerField(db_column='Tacleglisse', blank=True, null=True)  # Field name made lowercase.
        plongeon = models.IntegerField(db_column='Plongeon', blank=True, null=True)  # Field name made lowercase.
        jeumain = models.IntegerField(db_column='Jeumain', blank=True, null=True)  # Field name made lowercase.
        jeupied = models.IntegerField(db_column='Jeupied', blank=True, null=True)  # Field name made lowercase.
        placement_1 = models.IntegerField(db_column='Placement.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
        reflexes = models.IntegerField(db_column='Reflexes', blank=True, null=True)  # Field name made lowercase.
        
        class Meta :
                verbose_name = 'jugador'

        def __str__(self):
                return f'{self.nom} {self.gen} {self.valeur} '
        


class Equipo (models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        presupuesto = models.IntegerField(default=50000000)
        nombre = models.CharField(max_length=40, unique= True)
        categoria = models.CharField(max_length=10, default= 'E')


class Plantel (models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)
        jugador = models.ForeignKey(Fifa, on_delete=models.CASCADE)
        nombre = models.CharField(max_length=255, null=True)
        valor = models.IntegerField(null=True)
        general = models.IntegerField(null=True)
        pais = models.CharField(max_length=255, null=True)
        posicion = models.CharField(max_length=20, null=True)


        def __str__(self):
                return self.jugador.nom
                

class Clubes (models.Model):
        nombre = models.CharField(max_length=40)
        general = models.IntegerField()
        categoria = models.CharField(max_length=40, blank=True)


        def __str__(self):
                return f'{self.nombre} {self.general}'

class Torneo (models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        nombre = models.CharField(max_length=40, null= True, blank=True)
        gen = models.IntegerField(null= True, blank=True)
        cat = models.CharField(max_length=40, null=True, blank=True)

class Puntos (models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        club = models.ForeignKey(Torneo, on_delete=models.CASCADE)
        nombre = models.CharField(max_length=40, null=True)
        puntos_db = models.IntegerField()
        categoria = models.CharField(max_length=10)
        resultado_mio = models.IntegerField(null=True)
        resultado_rival = models.IntegerField(null=True)
