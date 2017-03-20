from django import forms
from home.models import NREL, NodeController
from django.core import serializers


class NREL_Times(forms.Form):
    timeStamps = forms.ModelChoiceField(queryset=NREL.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)
    queryset = NREL.objects.all()
    queryset2 = serializers.serialize('json', queryset)


class NREL_Form(forms.ModelForm):

    class Meta:
        model = NREL
        fields = ('timestamp', 'ghi', 'dni', 'air_temp', 'rel_humid', 'wind_speed', 'wind_dir', 'station_pressure')


    # Attributes
    timestamp = forms.CharField(label='Timestamp', max_length=50,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_timestamp'}))
    ghi = forms.CharField(label='Ghi', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_ghi'}))
    dni = forms.CharField(label='Dni', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_dni'}))
    dhi = forms.CharField(label='Dhi', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_dhi'}))
    air_temp = forms.CharField(label='Air Temp', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_air_temp'}))
    rel_humid = forms.CharField(label='Rel humid', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_rel_humid'}))
    wind_speed = forms.CharField(label='Wind speed', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_wind_speed'}))
    wind_dir = forms.CharField(label='Wind dir', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_wind_dir'}))
    station_pressure = forms.CharField(label='Station pressure', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_station_pressure'}))


class GetNodes(forms.Form):
    queryset = NodeController.objects.all()
    queryset2 = serializers.serialize('json', queryset)



# class BatteryForm(forms.ModelForm):
#     class Meta:
#         model = NREL
#         fields = (
#             'nc_id',
#             'manufacturer',
#             'dimension',
#             'weight',
#             'R',
#             'capacity',
#             'roundtrip_efficiency',
#             'min_soc',
#             'max_charging_rate',
#             'max_discharing_rate',
#             'charging_efficiency'
#             'discharging_efficiency',
#             'required_reserve',
#             'rated_voltage',
#             'phase',
#             'current_voltage'
#         )
#
#     # Attributes
#     timestamp = forms.CharField(label='Nc_id', max_length=50,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_nc_id'}))
#     ghi = forms.CharField(label='Manufacturer', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_manufacturer'}))
#     dni = forms.CharField(label='Dimension', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_dimension'}))
#     dhi = forms.CharField(label='Weight', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_weight'}))
#     air_temp = forms.CharField(label='R', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_R'}))
#     rel_humid = forms.CharField(label='Capacity', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_Capacity'}))
#     wind_speed = forms.CharField(label='Rountrip Efficiency', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_roundtrip'}))
#     wind_dir = forms.CharField(label='Max Charging Rate', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_max_charging_rate'}))
#     station_pressure = forms.CharField(label='Max Discharing Rate', max_length=30,
#                           widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name': 'Nrel_charging_efficiency'}))