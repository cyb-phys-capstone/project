from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(NodeController)
admin.site.register(Battery)
admin.site.register(Generator)
admin.site.register(Inverter)
