from django.shortcuts import render, render_to_response, get_object_or_404
from home.forms import *
<<<<<<< HEAD
from home.models import NREL, NodeController, Battery, BData, Generator, Inverter, IData, Solar, SData


# Create your views here.
def nrel_times(request):
    form = NREL_Times()
    return render(request, 'client/nrel.html', {'form': form})


def nrel_view(request):
    try:
        comp = NREL.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = NREL.objects.values().first()
=======
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
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
    form = NREL_Form(initial=comp)
    return render(request, 'client/nrelView.html', {'form': form})


def battery_times(request):
    form = Battery_Times()
    return render(request, 'client/battery.html', {'form': form})


def battery_view(request):
    try:
        comp = BData.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = BData.objects.values().first()
    form = Battery_Form(initial=comp)
    return render(request, 'client/batteryView.html', {'form': form})


def inverter_times(request):
    form = Inverter_Times()
    return render(request, 'client/inverter.html', {'form': form})


def inverter_view(request):
    try:
        comp = IData.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = IData.objects.values().first()
    form = Inverter_Form(initial=comp)
    return render(request, 'client/inverterView.html', {'form':form})


def generator_times(request):
    form = Generator_Times()
    return render(request, 'client/generator.html',{'form':form})


def generator_view(request):
    try:
        comp = GData.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = GData.objects.values().first()
    form = Generator_Form(initial=comp)
    return render(request, 'client/generatorView.html', {'form': form})


def inverter_template(request):
    return render(request, 'client/DeviceInfo/InverterTemplate.html')


def node_template(request):
    return render(request, 'client/DeviceInfo/NodeTemplate.html')


def asset_template(request):
    return render(request, 'client/asset_template.html')


def solar_times(request):
    form=Solar_Times()
    return render (request, 'client/solar.html',{'form':form})


def solar_view(request):
    try:
        comp = SData.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = SData.objects.values().first()
    form = Solar_Form(initial=comp)
    return render(request, 'client/solarView.html', {'form': form})


def treeDoodle(request):
    form = PopulateTree()
    print(form)
    return render(request, 'client/Tree/tree.html',
                  {
                      'form': form
                  }
                  )

<<<<<<< HEAD
=======

def battery_data(request):
    return render(request, 'client/DeviceInfo/BatteryTemplate.html')


def generator_template(request):
    return render(request, 'client/DeviceInfo/GeneratorTemplate.html')


def inverter_template(request):
    return render(request, 'client/DeviceInfo/InverterTemplate.html')


def node_template(request):
    return render(request, 'client/DeviceInfo/NodeTemplate.html')


>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
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
<<<<<<< HEAD
                    'solarHTML':solars,
                    'button': ' <button type="button">Click Me!</button> '
                   }
                  )
=======
                    'button': ' <button type="button">Click Me!</button> '
                   }
                  )

>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
