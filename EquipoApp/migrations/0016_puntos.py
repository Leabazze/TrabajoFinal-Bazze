# Generated by Django 4.2.5 on 2023-10-05 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EquipoApp', '0015_alter_clubes_categoria_alter_torneo_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puntos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos_db', models.IntegerField()),
                ('categoria', models.CharField(max_length=10)),
                ('resultado_mio', models.IntegerField(null=True)),
                ('resultado_rival', models.IntegerField(null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EquipoApp.torneo')),
            ],
        ),
    ]
