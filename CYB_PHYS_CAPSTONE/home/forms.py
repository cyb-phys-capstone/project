from django import forms
from home.models import NREL, NodeController, BData, GData
from django.core import serializers


class Generator_Times(forms.Form):
    timeStamps = forms.ModelChoiceField(queryset=GData.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)
    queryset = GData.objects.all()
    try:
        queryset2 = serializers.serialize('json', queryset)
    except:
        print("Can't get GDatas");

class Generator_Form(forms.ModelForm):

    class Meta:
        model = GData
        fields = ('timestamp','voltage','current','real_power_kw','real_power_kvar','frequency')

    #Attributes
    timestamp = forms.CharField(label='Timestamp',max_length=50,
                        widget=forms.TextInput(attrs={'class':'generator-attr','name':'Generator_timestamp'}))
    voltage = forms.CharField(label='Voltage (V)',max_length=30,
                        widget=forms.TextInput(attrs={'class':'generator-attr','name':'Generator_voltage'}))
    current = forms.CharField(label='Current (A)',max_length=30,
                        widget=forms.TextInput(attrs={'class':'generator-attr','name':'Generator_current'}))
    real_power_kw = forms.CharField(label='Real Power (kW)', max_length=30,
                        widget=forms.TextInput(attrs={'class':'generator-attr', 'name':'Generator_real_power_kw'}))
    real_power_kvar = forms.CharField(label='Real Power (kVAR)', max_length=30,
                                    widget=forms.TextInput(
                                        attrs={'class': 'generator-attr', 'name': 'Generator_real_power_kvar'}))
    frequency = forms.CharField(label='Frequency (Hz)', max_length=30,
                                    widget=forms.TextInput(
                                        attrs={'class': 'generator-attr', 'name': 'Generator_frequency'}))

class Battery_Times(forms.Form):
    timeStamps = forms.ModelChoiceField(queryset=BData.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)
    queryset = BData.objects.all()
    try:
        queryset2 = serializers.serialize('json', queryset)
    except:
        print("Can't get BDatas")

class Battery_Form(forms.ModelForm):

    class Meta:
        model = BData
        fields = ('timestamp','current_soc','current_voltage','current_kw','current_kvar', 'state')

    # Attributes
    timestamp = forms.CharField(label='Timestamp', max_length=50,
                          widget=forms.TextInput(attrs={'class': 'battery-attr', 'name':'Battery_timestamp'}))
    current_soc = forms.CharField(label='SOC (%)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'battery-attr', 'name':'Battery_soc'}))
    current_voltage = forms.CharField(label='Voltage (V)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'battery-attr', 'name':'Battery_voltage'}))
    current_kw = forms.CharField(label='KW (kW)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'battery-attr', 'name':'Battery_kw'}))
    current_kvar = forms.CharField(label='KVAR (kVAR)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'battery-attr', 'name':'Battery_kvar'}))
    state = forms.CharField(label='State', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'battery-attr', 'name':'Battery_state'}))


class NREL_Times(forms.Form):
    timeStamps = forms.ModelChoiceField(queryset=NREL.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)
    queryset = NREL.objects.all()
    try:
        queryset2 = serializers.serialize('json', queryset)
    except:
        print("Can't get NRELs")


class NREL_Form(forms.ModelForm):

    class Meta:
        model = NREL
        fields = ('timestamp', 'ghi', 'dni', 'air_temp', 'rel_humid', 'wind_speed', 'wind_dir', 'station_pressure')

    # Attributes
    timestamp = forms.CharField(label='Timestamp', max_length=50,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_timestamp'}))
    ghi = forms.CharField(label='GHI (W/m^2)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_ghi'}))
    dni = forms.CharField(label='DNI (W/m^2)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_dni'}))
    dhi = forms.CharField(label='DHI (W/m^2)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_dhi'}))
    air_temp = forms.CharField(label='Air Temp (*C)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_air_temp'}))
    rel_humid = forms.CharField(label='Rel. Humid (%)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_rel_humid'}))
    wind_speed = forms.CharField(label='Wind Speed (m/s)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_wind_speed'}))
    wind_dir = forms.CharField(label='Wind Dir (*N)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_wind_dir'}))
    station_pressure = forms.CharField(label='Station Pressure (mBar)', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'asset-attr', 'name':'Nrel_station_pressure'}))


class GetNodes(forms.Form):
    queryset = NodeController.objects.all()
    try:
        queryset2 = serializers.serialize('json', queryset)
    except:
        print("Can't get NodeControllers")


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
