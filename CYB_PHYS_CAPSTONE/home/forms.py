from django import forms
from home.models import NREL, NodeController, BData, GData, Generator, Inverter, IData, Battery, SData
from django.core import serializers

class PopulateTree:
    nodes_from_db = NodeController.objects.all()
    generators_from_db = Generator.objects.all()
    inverters_from_db = Inverter.objects.all()
    battery_from_db = Battery.objects.all()
    b_data_from_db = BData.objects.all()
    i_data_from_db = IData.objects.all()
    g_data_from_db = GData.objects.all()
    try:
        nodes = serializers.serialize('json', nodes_from_db)
        generators = serializers.serialize('json', generators_from_db)
        inverters = serializers.serialize('json', inverters_from_db)
        batteries = serializers.serialize('json', battery_from_db)
        bdata = serializers.serialize('json', b_data_from_db)
        idata = serializers.serialize('json', i_data_from_db)
        gdata = serializers.serialize('json', g_data_from_db)
    except:
        print("could not find devices")

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


class Inverter_Times(forms.Form):
    timestamps = forms.ModelChoiceField(queryset=IData.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)
    queryset = IData.objects.all()
    try:
        queryset2 = serializers.serialize('json', queryset)
    except:
        print("Can't get IDatas")


class Inverter_Form(forms.ModelForm):
    class Meta:
        model = IData
        fields = ('timestamp','output_voltage','real_power','reactive_power','frequency','input_voltage','dc_power','battery_charge_volt','power_factor')

    #Attributes
    output_voltage = forms.CharField(label='Output Voltage (kV)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_output_voltage'}))
    real_power = forms.CharField(label='Real Power (kW)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_real_power'}))
    reactive_power = forms.CharField(label='Reactive Power (kVAR)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_reactive_power'}))
    frequency = forms.CharField(label='Frequency (Hz)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_frequency'}))
    input_voltage = forms.CharField(label='Input Voltage (V)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_input_voltage'}))
    dc_power = forms.CharField(label='DC Power (kW)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_dc_power'}))
    battery_charge_volt = forms.CharField(label='Battery Charging Voltage (V)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_battery_charge_volt'}))
    power_factor = forms.CharField(label='Power Factor (%)',max_length=30,widget=forms.TextInput(attrs={'class':'asset-attr','name':'Inverter_power_factor'}))


class Solar_Times(forms.Form):
    timeStamps = forms.ModelChoiceField(queryset=BData.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)
    queryset = SData.objects.all()
    try:
        queryset2 = serializers.serialize('json', queryset)
    except:
        print("Can't get SDatas")

class Solar_Form(forms.ModelForm):
    class Meta:
        model=SData
        fields=('timestamp','voltage','current', 'real_power_kw')

    #Attributes
    voltage = forms.CharField(label='Voltage (V)', max_length=30,
                             widget=forms.TextInput(attrs={'class':'solar-attr','name':'Solar_voltage'}))
    current = forms.CharField(label='Current (A)',max_length=30,
                        widget=forms.TextInput(attrs={'class':'solar-attr','name':'Solar_current'}))
    real_power_kw = forms.CharField(label='Real Power (kW)', max_length=30,
                        widget=forms.TextInput(attrs={'class':'solar-attr', 'name':'Solar_real_power_kw'}))

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
