from django.shortcuts import render
from home.forms import *

# Create your views here.
def index(request):
    form = NREL_Times(initial=NREL.objects.values()[0]);
    return render(request, 'client/NREL.html', {'form':form})

def nrel (request):
    comp = NREL.objects.filter(wind_dir=171.0).values()[0]
    form = NREL_Form(initial=comp)
    return render(request, 'client/NRELview.html', {'form': form})

def DeviceData (request):
    return render(request, 'client/DeviceData.html')