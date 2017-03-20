from django.shortcuts import render, render_to_response, get_object_or_404
from home.forms import *
from home.models import NREL, NodeController, Battery, Generator, Inverter

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


def battery_data(request):
    return render(request, 'client/DeviceInfo/BatteryTemplate.html')


def generator_template(request):
    return render(request, 'client/DeviceInfo/GeneratorTemplate.html')


def inverter_template(request):
    return render(request, 'client/DeviceInfo/InverterTemplate.html')


def node_template(request):
    return render(request, 'client/DeviceInfo/NodeTemplate.html')


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

