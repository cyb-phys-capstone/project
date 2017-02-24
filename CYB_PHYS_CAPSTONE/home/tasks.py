# Required file for Celery
# Create your tasks here
from __future__ import absolute_import
from celery import shared_task
from .models import NREL
from lxml import html
from datetime import date, datetime
import requests

# Corresponding instances for NREL points
GHI_INST       = '4'
DNI_INST       = '5'
DHI_INST       = '6'
AIR_TEMP_INST  = '7'
REL_HUMID_INST = '8'
WIND_SPD_INST  = '9'
WIND_DIR_INST  = '11'
STN_PRES_INST  = '12'

# Get current date
today = date.today()
year  = str(today.year);
month = str(today.month);
day   = str(today.day);

# Gets the timestamp of the latest NREL data
def get_nrel_timestamp():
    # Make the HTTP request
    page = requests.get('http://www.nrel.gov/midc/apps/plot.pl?site=UAT;start=20101103;live=1;time=0;inst=0;type=data;first=3;math=0;second=-1;value=0.0;user=0;axis=1;endyear=' + year + ';endmonth=' + month + ';endday=' + day)
    # Parse the HTML
    tree = html.fromstring(page.content)
    # Get the raw text content
    content = tree.text_content()
    # Find the last occurence of comma
    # This gives us the most up to date value
    k = content.rfind(',')
    # Get the HH:MM value
    value_str = content[k-5:][:-6]
    # Create datetime from that
    d = datetime.strptime(value_str, '%H:%M')
    # Replace default year/month/day with current
    d = d.replace(year=date.today().year, month=date.today().month, day=date.today().day)
    return d

# Gets the NREL data for a requested item
def get_nrel_value(data_point):
    try:
        # Make the HTTP request
        page = requests.get('http://www.nrel.gov/midc/apps/plot.pl?site=UAT;start=20101103;live=1;time=0;inst=' + data_point + ';type=data;first=3;math=0;second=-1;value=0.0;user=0;axis=1;endyear=' + year + ';endmonth=' + month + ';endday=' + day)
        # Parse the HTML
        tree = html.fromstring(page.content)
        # Get the raw text content
        content = tree.text_content()
        # Find the last occurence of comma
        # This gives us the most up to date value
        k = content.rfind(',')
        value_str = content[k+1:]
    except requests.exceptions.RequestException as e:
        print(e)
        value_str = '0'
    return float(value_str)

@shared_task
def scrape_nrel():
    # Get the data
    ghi = get_nrel_value(GHI_INST)
    dni = get_nrel_value(DNI_INST)
    dhi = get_nrel_value(DHI_INST)
    air_temp = get_nrel_value(AIR_TEMP_INST)
    rel_humid = get_nrel_value(REL_HUMID_INST)
    wind_speed = get_nrel_value(WIND_SPD_INST)
    wind_dir = get_nrel_value(WIND_DIR_INST)
    stn_pres = get_nrel_value(STN_PRES_INST)

    # Get timestamp
    timestamp = get_nrel_timestamp()

    # Create object for model
    return NREL.objects.create(timestamp=timestamp,ghi=ghi,dni=dni,dhi=dhi,air_temp=air_temp,rel_humid=rel_humid,wind_speed=wind_speed,wind_dir=wind_dir,station_pressure=stn_pres)
