# Generated by Django 4.2.3 on 2023-09-29 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EquipoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantel',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EquipoApp.equipo'),
        ),
    ]
