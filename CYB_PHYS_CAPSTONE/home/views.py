from django.shortcuts import render, render_to_response, get_object_or_404
from home.forms import *
from home.models import NREL, NodeController, Battery, BData, Generator, Inverter, Solar, SData

# Create your views here.
def nrel_times(request):
    form = NREL_Times()
    return render(request, 'client/nrel.html', {'form': form})


def nrel_view(request):
    try:
        comp = NREL.objects.filter(timestamp=request.GET['timestamp']).values().first()
    except:
        comp = NREL.objects.values().first()
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
                    'solarHTML':solars,
                    'button': ' <button type="button">Click Me!</button> '
                   }
                  )
