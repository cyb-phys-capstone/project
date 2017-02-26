from django.shortcuts import render
from home.forms import *

# Create your views here.
def index(request):
    form = NREL_Times();
    return render(request, 'client/NREL.html', {'form':form})
