# Generated by Django 4.2.5 on 2023-10-09 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquipoApp', '0025_plantel_usuario_puntos_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantel',
            name='posicion',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
