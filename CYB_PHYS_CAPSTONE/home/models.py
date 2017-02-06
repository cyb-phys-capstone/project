from __future__ import unicode_literals

import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.


class CollectsFrom(models.Model):
    date = models.DateField(primary_key=True,default=datetime.date.today)


class NodeControllers(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type= models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    a_id = GenericForeignKey('content_type','object_id')
    model = models.CharField(max_length=15, default="")
    manufacturer = models.CharField(max_length=20, default="")


class Batteries(models.Model):
    id = models.IntegerField(primary_key=True)
    nc_id = models.ForeignKey('NodeControllers',on_delete=models.CASCADE)
    max_battery_voltage = models.FloatField(default=0.0)
    time_in_float = models.FloatField(default=0.0)
    max_current = models.FloatField(default=0.0)
    accum_amp_hours = models.FloatField(default=0.0)
    min_batt_volt_absorb_time = models.FloatField(default=0.0)
    model = models.CharField(max_length=15,default="")
    manufacturer = models.CharField(max_length=20, default="")


class Generators(models.Model):
    id = models.IntegerField(primary_key=True)
    nc_id = models.ForeignKey('NodeControllers', on_delete=models.CASCADE)
    frequency = models.FloatField(default=0.0)
    voltage = models.FloatField(default=0.0)
    temperature = models.FloatField(default=0.0)
    dc_power_rate = models.FloatField(default=0.0)
    ampHours = models.FloatField(default=0.0)
    kWProduction = models.FloatField(default=0.0)
    model = models.CharField(max_length=15, default="")
    manufacturer = models.CharField(max_length=20, default="")
    fuel_type = models.CharField(max_length=15, default="")


class Inverters(models.Model):
    id = models.IntegerField(primary_key=True)
    nc_id = models.ForeignKey('NodeControllers',on_delete=models.CASCADE)
    dc_input = models.FloatField(default=0.0)
    ac_output = models.FloatField(default=0.0)
    model = models.CharField(max_length=15, default="")
    manufacturer = models.CharField(max_length=20, default="")


class BData(models.Model):
    id = models.IntegerField(primary_key=True)
    b_id = models.ForeignKey('Batteries',on_delete=models.CASCADE)
    collected = models.ForeignKey('CollectsFrom',models.CASCADE)
    amps = models.FloatField(default=0.0)


class GData(models.Model):
    id = models.IntegerField(primary_key=True)
    g_id = models.ForeignKey('Generators', on_delete=models.CASCADE)
    collected = models.ForeignKey('CollectsFrom', models.CASCADE)
    amps = models.FloatField(default=0.0)


class IData(models.Model):
    id = models.IntegerField(primary_key=True)
    i_id = models.ForeignKey('Inverters',on_delete=models.CASCADE)
    collected = models.ForeignKey('CollectsFrom', models.CASCADE)
    amps = models.FloatField(default=0.0)
    amp_hours = models.FloatField(default=0.0)
    peak_watts = models.FloatField(default=0.0)
    solar_array_voltage = models.FloatField(default=0.0)