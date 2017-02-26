from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.db.models import Sum, Q
from django.contrib.auth.models import User
from home.models import NREL


class NREL_Times(forms.Form):
    timeStamps = forms.ModelChoiceField(queryset=NREL.objects.datetimes('timestamp', 'second'), widget=forms.Select, empty_label=None)



class NREL_Form(forms.Form):

    class Meta:
        model = NREL
        fields = ('time', 'date', 'ghi', 'dni', 'air_temp', 'rel_humid', 'wind_speed', 'wind_dir', 'station_pressure')

    timeStamps = forms.ModelChoiceField(queryset=NREL.objects.all(), widget=forms.RadioSelect, empty_label=None)

    # timeStamp
    time = forms.CharField(label='Time', max_length=30,
                           widget=forms.TextInput(attrs={'class':'nrel-timeStamp', 'name':'timeStamp_time'}))
    date = forms.CharField(label='Date', max_length=30,
                           widget=forms.TextInput(attrs={'class': 'nrel-timestamp', 'name':'timeStamp_date'}))

    # Attributes
    ghi = forms.CharField(label='Ghi', max_length=30,
                          widget=forms.TextInput(attrs={'class': 'nrel-attr', 'name':'Nrel_ghi'}))
