from django.shortcuts import render
from home.forms import *

# Create your views here.
def index(request):
    form = NREL_Form();
    return render(request, 'client/NREL.html', {'form':form})
