from django.shortcuts import render, render_to_response, get_object_or_404
from home.forms import *
from home.models import NREL, NodeController, Battery, BData, Generator, Inverter

# Create your views here.
def nrel_times(request):
    form = NREL_Times()
    return render(request, 'client/NREL.html', {'form': form})


def nrel_view(request):
    try:
        comp = NREL.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = NREL.objects.values().first()
    form = NREL_Form(initial=comp)
    return render(request, 'client/NRELview.html', {'form': form})


def battery_times(request):
    form = Battery_Times()
    return render(request, 'client/battery.html', {'form': form})


def battery_view(request):
    try:
        comp = BData.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = BData.objects.values().first()
    form = Battery_Form(initial=comp)
    return render(request, 'client/battery.html', {'form': form})


def generator_template(request):
    return render(request, 'client/DeviceInfo/GeneratorTemplate.html')


def inverter_template(request):
    return render(request, 'client/DeviceInfo/InverterTemplate.html')


def node_template(request):
    return render(request, 'client/DeviceInfo/NodeTemplate.html')

def asset_template(request):
    return render(request, 'client/asset_template.html')


def treeDoodle(request):
    return render(request, 'client/Tree/tree.html')


def device_selector(request):
    nodes = NodeController.objects.all()
    generators = Generator.objects.all()
    inverters = Inverter.objects.all()
    batteries = Battery.objects.all()
    return render(request, 'client/DeviceSelector.html',
                  {
                    'nodesHTML': nodes,
                    'generatorHTML': generators,
                    'invertersHTML': inverters,
                    'batteriesHTML': batteries,
                    'button': ' <button type="button">Click Me!</button> '
                   }
                  )
