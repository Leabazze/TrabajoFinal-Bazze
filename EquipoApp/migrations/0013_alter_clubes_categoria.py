# Generated by Django 4.2.5 on 2023-10-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquipoApp', '0012_alter_clubes_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubes',
            name='categoria',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]