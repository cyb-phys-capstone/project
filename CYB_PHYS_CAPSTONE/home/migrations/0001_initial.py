# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 19:51
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(default='', max_length=20)),
                ('dimension', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None), size=None)),
                ('weight', models.FloatField(verbose_name=models.FloatField(default=0.0))),
                ('R', models.FloatField(default=0.0)),
                ('capacity', models.FloatField(default=24.0)),
                ('rountrip_efficiency', models.FloatField(default=90.0)),
                ('min_soc', models.FloatField(default=20.0)),
                ('max_charging_rate', models.FloatField(default=1.0)),
                ('max_discharing_rate', models.FloatField(default=1.0)),
                ('charging_efficiency', models.FloatField(default=90.0)),
                ('discharging_efficiency', models.FloatField(default=90.0)),
                ('required_reserve', models.FloatField(default=20.0)),
                ('rated_voltage', models.FloatField(default=20.0)),
                ('phase', models.IntegerField(default=1)),
                ('current_voltage', models.FloatField(default=12.0)),
            ],
        ),
        migrations.CreateModel(
            name='BData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_soc', models.FloatField()),
                ('current_kw', models.FloatField()),
                ('current_kvar', models.FloatField()),
                ('state', models.IntegerField(default=0)),
                ('capacity', models.FloatField(default=24.0)),
                ('roundtrip_eff', models.FloatField(default=90.0)),
                ('min_soc', models.FloatField(default=20.0)),
                ('max_charging_rate', models.FloatField(default=1.0)),
                ('max_discharging_rate', models.FloatField(default=1.0)),
                ('charging_eff', models.FloatField(default=90.0)),
                ('discharging_eff', models.FloatField(default=90.0)),
                ('required_reserve', models.FloatField(default=20.0)),
                ('rated_voltage', models.FloatField(default=24.0)),
                ('phase', models.IntegerField(default=1)),
                ('current_voltage', models.FloatField(default=12.0)),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Battery')),
            ],
        ),
        migrations.CreateModel(
            name='CollectsFrom',
            fields=[
                ('date', models.DateField(default=datetime.date.today, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='GData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_voltage', models.FloatField()),
                ('output_current', models.FloatField()),
                ('output_real_power1', models.FloatField()),
                ('output_real_power2', models.FloatField()),
                ('frequency', models.FloatField()),
                ('collected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CollectsFrom')),
            ],
        ),
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(default='', max_length=20)),
                ('dimension', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None), size=None)),
                ('weight', models.FloatField(verbose_name=models.FloatField(default=0.0))),
                ('fuel_type', models.CharField(default='', max_length=15)),
                ('smart_control', models.BooleanField(default=False)),
                ('frequency', models.FloatField(default=60.0)),
                ('electrical_efficiency', models.FloatField(default=90.0)),
                ('thermal_efficiency', models.FloatField(default=90.0)),
                ('capacity', models.FloatField(default=1.0)),
                ('voltage', models.FloatField(default=110.0)),
                ('power_factor', models.FloatField(default=80.0)),
                ('phase', models.IntegerField(default=1)),
                ('max_real_power', models.FloatField()),
                ('min_real_power', models.FloatField()),
                ('max_reactive_power', models.FloatField()),
                ('min_reactive_power', models.FloatField()),
                ('max_voltage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_voltage', models.FloatField()),
                ('real_power', models.FloatField()),
                ('reactive_power', models.FloatField()),
                ('frequency', models.FloatField()),
                ('input_voltage', models.FloatField()),
                ('dc_power', models.FloatField()),
                ('battery_charge_volt', models.FloatField()),
                ('collected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CollectsFrom')),
            ],
        ),
        migrations.CreateModel(
            name='Inverter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(default='', max_length=20)),
                ('reactive_power_support', models.BooleanField(default=False)),
                ('battery_charging_support', models.BooleanField(default=False)),
                ('communication_protocol', models.CharField(default='', max_length=10)),
                ('islanding_capability', models.BooleanField(default=True)),
                ('grid_connectivity', models.BooleanField(default=True)),
                ('capacity', models.FloatField(default=1.0)),
                ('input_source', models.SmallIntegerField(default=0)),
                ('input_voltage', models.FloatField(default=24.0)),
                ('power_factor', models.FloatField(default=90.0)),
                ('efficiency', models.FloatField(default=100.0)),
                ('phase', models.IntegerField(default=1)),
                ('battery_charging_eff', models.FloatField(default=90.0)),
                ('frequency', models.FloatField(default=60.0)),
                ('max_real_power', models.FloatField()),
                ('max_reactive_power', models.FloatField()),
                ('max_voltage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='NodeController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('model', models.CharField(default='', max_length=15)),
                ('manufacturer', models.CharField(default='', max_length=20)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='NREL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('ghi', models.FloatField(default=0.0)),
                ('dni', models.FloatField(default=0.0)),
                ('dhi', models.FloatField(default=0.0)),
                ('air_temp', models.FloatField(default=0.0)),
                ('rel_humid', models.FloatField(default=0.0)),
                ('wind_speed', models.FloatField(default=0.0)),
                ('wind_dir', models.FloatField(default=0.0)),
                ('station_pressure', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='SData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_voltage', models.FloatField()),
                ('current', models.FloatField()),
                ('real_power', models.FloatField()),
                ('collected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CollectsFrom')),
            ],
        ),
        migrations.CreateModel(
            name='Solar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(default='', max_length=20)),
                ('dimension', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=None), size=None)),
                ('weight', models.FloatField(verbose_name=models.FloatField(default=0.0))),
                ('short_circuit_current', models.FloatField(default=5.0)),
                ('open_circuit_voltage', models.FloatField(verbose_name=21.0)),
                ('capacity', models.FloatField(verbose_name=1.0)),
                ('azimuth', models.FloatField(default=0.0)),
                ('slope', models.FloatField(default=33.45)),
                ('nc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.NodeController')),
            ],
        ),
        migrations.AddField(
            model_name='sdata',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Solar'),
        ),
        migrations.AddField(
            model_name='inverter',
            name='nc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.NodeController'),
        ),
        migrations.AddField(
            model_name='idata',
            name='i_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Inverter'),
        ),
        migrations.AddField(
            model_name='generator',
            name='nc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.NodeController'),
        ),
        migrations.AddField(
            model_name='gdata',
            name='g_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Generator'),
        ),
        migrations.AddField(
            model_name='bdata',
            name='collected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CollectsFrom'),
        ),
        migrations.AddField(
            model_name='battery',
            name='nc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.NodeController'),
        ),
    ]
