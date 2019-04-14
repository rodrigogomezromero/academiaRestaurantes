# Generated by Django 2.2 on 2019-04-13 02:25

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre de categoria')),
            ],
            bases=(models.Model, core.models.Timestamps),
        ),
        migrations.CreateModel(
            name='Flavors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre del sabor')),
            ],
            bases=(models.Model, core.models.Timestamps),
        ),
        migrations.CreateModel(
            name='Resturantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, core.models.Timestamps),
        ),
        migrations.CreateModel(
            name='UnitsMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre de la unidad de medida')),
            ],
            bases=(models.Model, core.models.Timestamps),
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre del platillo')),
                ('description', models.TextField(default='', max_length=500, null=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Precio del platillo')),
                ('categories', models.ManyToManyField(to='core.Categories')),
                ('flavors', models.ManyToManyField(to='core.Flavors')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='core.Resturantes')),
                ('unit_measure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.UnitsMeasure')),
            ],
            bases=(models.Model, core.models.Timestamps),
        ),
    ]