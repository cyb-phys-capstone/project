"""CYB_PHYS_CAPSTONE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^asset_template/', views.asset_template),
    url(r'^nrel/', views.nrel_times),
    url(r'^nrel_view/', views.nrel_view),
    url(r'^battery/', views.battery_times),
    url(r'^battery_view/', views.battery_view),
    url(r'^generator/',views.generator_times),
    url(r'^generator_view/', views.generator_view),
    url(r'^inverter/', views.inverter_times),
    url(r'^inverter_view/', views.inverter_view),
    url(r'^solar/', views.solar_times),
    url(r'^solar_view',views.solar_view),
    url(r'^NodeTemplate/', views.node_template),
    url(r'^DeviceSelector/', views.device_selector),
    url(r'^tree/devicemapdata/', views.device_map_getrequest),
    url(r'^tree/', views.treeDoodle),
    url(r'^$', views.treeDoodle)
]
