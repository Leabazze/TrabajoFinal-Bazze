# Generated by Django 4.2.5 on 2023-10-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquipoApp', '0019_torneo_puntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntos',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
    ]