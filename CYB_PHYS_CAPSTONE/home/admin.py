from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(NodeController)
#admin.site.register(CollectsFrom)
admin.site.register(Battery)
admin.site.register(Generator)
admin.site.register(Inverter)
admin.site.register(Solar)
admin.site.register(BData)
admin.site.register(GData)
admin.site.register(IData)
admin.site.register(SData)
admin.site.register(NREL)
