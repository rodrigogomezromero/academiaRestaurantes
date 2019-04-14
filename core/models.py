from django.db import models
import datetime
# Create your models here.


class Timestamps:

    create_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)
    delated_at = models.DateTimeField(verbose_name='Fecha de borrado', blank=True, null=True)


class Shedules(models.Model):
    DAYS = (
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miercoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
        (7, 'Domingo')
    )

    day = models.CharField(choices=DAYS, verbose_name='Dia de la semana', max_length=100)
    time_open = models.TimeField(verbose_name='Hora de apertura', null=True)
    time_close = models.TimeField(verbose_name='Hora de Cierre', null=True)
    closed = models.BooleanField(default=False)


class Resturants(models.Model, Timestamps):
    KINDS_REST = (
        (1, 'Estableciminto'),
        (2, 'Ambulante'),
        (3, 'Online'),
    )

    name = models.CharField(max_length=200, null=False, verbose_name='Nombre del restaurante')
    address = models.TextField(max_length=400, blank=True, null=True, verbose_name='Dirección del establecimiento')
    logo_url = models.URLField(verbose_name='Ruta del logo', null=True)
    sitio_web = models.URLField(verbose_name='Sitio web', null=True)
    horarios = models.ManyToManyField(Shedules)


class Categories(models.Model, Timestamps):
    name = models.CharField(max_length=255, null=False, verbose_name='Nombre de categoria')

    def __str__(self):
        return self.name


class Flavors(models.Model, Timestamps):
    name = models.CharField(max_length=255,null=False, verbose_name='Nombre del sabor')

    def __str__(self):
        return self.name


class UnitsMeasure(models.Model, Timestamps):
    name = models.CharField(max_length=255, null=False, verbose_name='Nombre de la unidad de medida')

    def __str__(self):
        return self.name


class Dishes(models.Model, Timestamps):
    name = models.CharField(max_length=255, null=False, verbose_name='Nombre del platillo')
    description = models.TextField(max_length=500, null=True, default='', verbose_name='Descripción')
    price = models.DecimalField(verbose_name='Precio del platillo', decimal_places=2, max_digits=8, null=False, default=0.0)
    unit_measure = models.ForeignKey(UnitsMeasure, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Resturants, on_delete=models.CASCADE, related_name='restaurant')
    categories = models.ManyToManyField(Categories)
    flavors = models.ManyToManyField(Flavors)

    def __str__(self):
        return "{name} ({price}".format(name=self.name, desc=self.description)

