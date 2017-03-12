from django.shortcuts import render
from home.forms import *


# Create your views here.
def index(request):
    form = NREL_Times()
    return render(request, 'client/NREL.html', {'form': form})


def nrel(request):
    try:
        comp = NREL.objects.filter(timestamp=request.GET['timestamp']).values()[0]
    except:
        comp = NREL.objects.values()[0]
    form = NREL_Form(initial=comp)
    return render(request, 'client/NRELview.html', {'form': form})


def DeviceData (request):
    return render(request, 'client/DeviceData.html')