# Generated by Django 4.2.3 on 2023-10-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquipoApp', '0008_alter_equipo_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('general', models.IntegerField()),
            ],
        ),
    ]
