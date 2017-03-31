from __future__ import unicode_literals

import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


#class CollectsFrom(models.Model):
#    date = models.DateField(primary_key=True,default=datetime.date.today)


class NodeController(models.Model):
    #id = models.IntegerField(primary_key=True)
    content_type= models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    a_id = GenericForeignKey('content_type','object_id')
    model = models.CharField(max_length=15, default="")
    manufacturer = models.CharField(max_length=20, default="")


class Battery(models.Model):
    #id = models.IntegerField(primary_key=True)
    nc_id = models.ForeignKey('NodeController',on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=20, default="")
    dimension = ArrayField(ArrayField(ArrayField(models.FloatField(default=0.0)))) #unit: meter
    weight = models.FloatField(default=0.0) #unit: kg
    R = models.FloatField(default=0.0) #unit: %
    capacity = models.FloatField(default=24.0) #unit: kWh
    rountrip_efficiency = models.FloatField(default=90.0) #unit: %
    min_soc = models.FloatField(default=20.0) #unit: %
    max_charging_rate = models.FloatField(default=1.0) #unit: C
    max_discharing_rate = models.FloatField(default=1.0) #unit: C
    charging_efficiency = models.FloatField(default=90.0) #unit: %
    discharging_efficiency = models.FloatField(default=90.0) #unit: %
    required_reserve = models.FloatField(default=20.0) #unit: %
    rated_voltage = models.FloatField(default=20.0) #unit: V
    phase = models.IntegerField(default=1)
    current_voltage = models.FloatField(default=12.0) #unit: V


class Generator(models.Model):
    #id = models.IntegerField(primary_key=True)
    nc_id = models.ForeignKey('NodeController', on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=20, default="")
    dimension = ArrayField(ArrayField(ArrayField(models.FloatField(default=0.0)))) #unit: meter
    weight = models.FloatField(default=0.0) #unit: kg
    fuel_type = models.CharField(max_length=15, default="")
    smart_control = models.BooleanField(default=False)
    frequency = models.FloatField(default=60.0) #unit: Hz
    electrical_efficiency = models.FloatField(default=90.0) #unit: %
    thermal_efficiency = models.FloatField(default=90.0) #unit: %
    capacity = models.FloatField(default=1.0) #unit: kW
    voltage = models.FloatField(default=110.0) #unit: V
    power_factor = models.FloatField(default=80.0) #unit: %
    phase = models.IntegerField(default=1)
    max_real_power = models.FloatField() #unit: kW
    min_real_power = models.FloatField() #unit: kW
    max_reactive_power = models.FloatField() #unit: kVAR
    min_reactive_power = models.FloatField() #unit: kVAR
    max_voltage = models.FloatField() #unit: V


class Inverter(models.Model):
    #id = models.IntegerField(primary_key=True)
    nc_id = models.ForeignKey('NodeController',on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=20, default="")
    reactive_power_support = models.BooleanField(default=False)
    battery_charging_support = models.BooleanField(default=False)
    communication_protocol = models.CharField(default="",max_length=10)
    islanding_capability = models.BooleanField(default=True)
    grid_connectivity = models.BooleanField(default =True)
    capacity = models.FloatField(default=1.0) #unit: kW
    input_source = models.SmallIntegerField(default=0)
    input_voltage = models.FloatField(default=24.0) #unit: V
    power_factor = models.FloatField(default=90.0) #unit: %
    efficiency = models.FloatField(default=100.0) #unit: %
    phase = models.IntegerField(default=1)
    battery_charging_eff =models.FloatField(default=90.0) #unit: %
    frequency =models.FloatField(default=60.0) #unit: Hz
    max_real_power = models.FloatField() #unit: kW
    max_reactive_power = models.FloatField() #unit: kVAR
    max_voltage = models.FloatField() #unit: V


class Solar(models.Model):
    nc_id = models.ForeignKey('NodeController',on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=20, default="")
    dimension = ArrayField(ArrayField(ArrayField(models.FloatField(default=0.0)))) # unit: meter
    weight = models.FloatField(default=0.0) #unit:kg
    short_circuit_current = models.FloatField(default=5.0) #unit: A
    open_circuit_voltage = models.FloatField(21.0) #unit:V
    capacity = models.FloatField(1.0) #unit: kW
    azimuth = models.FloatField(default=0.0) #unit: degrees
    slope = models.FloatField(default=33.45) #unit: degrees


class BData(models.Model):
    #id = models.IntegerField(primary_key=True)
    b_id = models.ForeignKey('Battery',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
#    collected = models.ForeignKey('CollectsFrom',models.CASCADE)
    current_soc = models.FloatField() #unit: %
    current_voltage = models.FloatField() #unit: V
    current_kw = models.FloatField() #unit: kW
    current_kvar = models.FloatField() #unit: kVAR
    state = models.IntegerField(default=0)
    capacity = models.FloatField(default=24.0) #unit: kWh
    roundtrip_eff = models.FloatField(default=90.0) #unit: %
    min_soc = models.FloatField(default=20.0) #unit: %
    max_charging_rate = models.FloatField(default=1.0) #unit: C
    max_discharging_rate = models.FloatField(default=1.0) #unit: C
    charging_eff = models.FloatField(default=90.0) #unit: %
    discharging_eff = models.FloatField(default=90.0) #unit: %
    required_reserve = models.FloatField(default=20.0) #unit: %
    rated_voltage = models.FloatField(default=24.0) #unit: V
    phase = models.IntegerField(default=1)
    current_voltage = models.FloatField(default=12.0) #unit: V


class GData(models.Model):
    #id = models.IntegerField(primary_key=True)
    g_id = models.ForeignKey('Generator', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
#    collected = models.ForeignKey('CollectsFrom', models.CASCADE)
    output_voltage = models.FloatField() #unit: V
    output_current = models.FloatField() #unit: A
    output_real_power1 = models.FloatField() #unit: kW
    output_real_power2 = models.FloatField() #unit: kVAR
    frequency = models.FloatField() #unit: Hz


class SData(models.Model):
    s_id = models.ForeignKey('Solar',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
#    collected = models.ForeignKey('CollectsFrom', models.CASCADE)
    output_voltage = models.FloatField() #unit: V
    current = models.FloatField() #unit: A
    real_power = models.FloatField() #unit: KW


class IData(models.Model):
    #id = models.IntegerField(primary_key=True)
    i_id = models.ForeignKey('Inverter',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
#    collected = models.ForeignKey('CollectsFrom', models.CASCADE)
    output_voltage = models.FloatField() #unit: kV
    real_power = models.FloatField() #unit: kW
    reactive_power = models.FloatField() #unit: kVAR
    frequency = models.FloatField() #unit: Hz
    input_voltage = models.FloatField() #unit: V
    dc_power = models.FloatField() #unit: kW
    battery_charge_volt = models.FloatField() #unit: V
    power_factor = models.FloatField #unit: %


class NREL(models.Model):
    #id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    ghi = models.FloatField(default=0.0)
    dni = models.FloatField(default=0.0)
    dhi = models.FloatField(default=0.0)
    air_temp = models.FloatField(default=0.0)
    rel_humid = models.FloatField(default=0.0)
    wind_speed = models.FloatField(default=0.0)
    wind_dir = models.FloatField(default=0.0)
    station_pressure = models.FloatField(default=0.0)
