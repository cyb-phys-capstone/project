from django import forms
from home.models import NREL


class NREL_Times(forms.Form):
    timeStamps = forms.ModelChoiceField(queryset=NREL.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)
    class Meta:
        model = NREL
        fields = ('timestamp', 'ghi', 'dni', 'air_temp', 'rel_humid', 'wind_speed', 'wind_dir', 'station_pressure')


    # Attributes
    timestamp = forms.CharField(label='Timestamp', max_length=50,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_timestamp'}))
    ghi = forms.CharField(label='GHI', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_ghi'}))
    dni = forms.CharField(label='DNI', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_dni'}))
    dhi = forms.CharField(label='DHI', max_length=30,
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
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_station_pressure', 'value': 0}))


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
