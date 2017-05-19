# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('apellido', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('domicilio', models.CharField(max_length=20)),
                ('vive_con', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('G', 'Ganador'), ('P', 'Preinscripto'), ('R', 'Rechazado'), ('C', 'Confirmado')], default='P', max_length=10)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='ficha',
            name='mama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mama', to='preinsc.Tutor'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='papa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='papa', to='preinsc.Tutor'),
        ),
    ]