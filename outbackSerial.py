import serial
from serial import SerialException
from datetime import date, datetime
import time
from ChargeController import ChargeController
from BatteryController import BatteryController
import psycopg2
from random import randint

# Make sure to change this depending on your system, this one is for mac
# linux will be something like "ttyAMA0/ACM0"
# windows will be something like "COM1"
# the baud rate should be 19200

#ser = serial.Serial("/dev/tty.usbmodem1421", 19200)

dt = datetime.now()
chargeID=randint(1, 1000000)
batteryID=randint(1, 10000000)

# main loop


def insertBattery():
	query = """INSERT INTO home_bdata (id, current_soc, current_kw, current_kvar, state, capacity, roundtrip_eff,
	min_soc, max_charging_rate, max_discharging_rate, charging_eff, discharging_eff, required_reserve, rated_voltage,
	phase, current_voltage, b_id_id, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
	return query
def insertCharge():
	query = """INSERT INTO home_sdata (id, output_voltage, current, real_power, s_id_id, timestamp) VALUES (%s, %s, %s, %s, %s, %s);"""
	return query

def createNodeController():
	query = """INSERT INTO home_nodecontroller (id, object_id, model, manufacturer, content_type_id) VALUES (%s, %s, %s, %s, %s, %s);"""
	return query

def createSolar():
	query = """INSERT INTO home_solar (id, manufracturer, dimension, weight, short_circuit_current, open_circuit_voltage, capacity, azimuth, slope, nc_id_id, model) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
	return query

def createBattery():
	query = """INSERT INTO home_battery (id, manufacturer, dimension, weight, R, capacity, rountrip_efficiency, min_soc, max_charging_rate, max_discharing_rate, charging_efficiency, discharging_efficiency, required_reserve, rated_voltage, phase, current_voltage, nc_id_id, model) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
	return query

try:
	conn = psycopg2.connect("dbname='CYB_PHYS_CAPSTONE_DB' user='admin' host='localhost' password='abc123' port='3306'")
	conn.autocommit = True
except:
	print("I am unable to connect to the database")


cursor = conn.cursor()

# for getting nformation on the tables, and their columns
#
#
#
# cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
# for table in cursor.fetchall():
# 	print(table)
cursor.execute("select column_name from information_schema.columns where table_name='home_bdata'")
column_names = [row[0] for row in cursor]
print (column_names)
cursor.execute("select column_name from information_schema.columns where table_name='home_battery'")
column_names = [row[0] for row in cursor]
print (column_names)
cursor.execute("""SELECT * FROM home_battery""")
print(cursor.fetchall())
print (dt)

try:
	cursor.execute(createNodeController(), (1, 1, "pi","raspberrypi", 9))
except:
	print("error trying to create node_controller")

try:
	cursor.execute(createNodeController(), (2, 1, 'pi',"raspberrypi", 12))
except:
	print("error trying to create node_controller")

# try:
# 	cursor.execute(createBattery(), (2,'outback', 34.0, 12, 0.0, 24.0, 90.0, 0.0, 1.0, 1.0, 90.0, 90.0, 20.0, 20.0, 1, 12.0, 1, 'Battery'))
# except:
# 	print("Failed to create a new battery object")
#
# try:
# 	cursor.execute(createSolar(), (2, 'outback', 34, 12, 5.0, 0.0, 24.0, 0.0, 33.45, 2, 'Solar'))
# except:
# 	print("Failed to create a new solar object")

def get_timestamp():
	# get full date currently
	now = datetime.now()
	# strip out the microseconds
	now_str = str(now).split(".")[0]
	# recreate date
	d = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
	return d


output ="00,4,0000,0126,0000,02,00023,287,099,001,00,33,062"
while 1:
	dt = get_timestamp()
	print(str(dt).split(".")[0])
	#output =ser.readline()
	if(len(output)>3):
		if(output[3]=='5'):
			deviceType="Inverter"
			print(output)
			#inverterData(deviceType, output)
		if(output[3]=='3'):
			chargeID+=1
			print(output)
			deviceType="Charge Controller"
			cc=ChargeController()
			cc.chargeControl(array=output,deviceType=deviceType)
			cursor.execute(insertCharge(), (chargeID,cc.pvVoltage, cc.chargeCurrent, 0.0, 1, dt))
			conn.commit()
		if(output[3]=='4'):
			batteryID+=1
			print(output)
			deviceType="DC Battery Monitor"
			bc= BatteryController()
			bc.batteryDC(deviceType=deviceType, array=output)
			print(bc.shuntAKillo)
			cursor.execute(insertBattery(),(batteryID, bc.stateOfCharge, bc.shuntAKillo, 12.0, 2.0, 24.0, 90.0, bc.minSOC, 1.0, 1.0, bc.netInputAH, bc.netOutputAH, 20.0, 24.0, 1, bc.batteryVoltage, 1, dt))
			conn.commit()
			#print(output, deviceType)
		time.sleep(5)


# this is for testing purposes (do not remove)
# output = "00,3,00,08,06,034,031,00,05,000,02,262,000,000,045"
# output = "00,4,0000,0126,0000,02,00023,287,099,001,00,33,062"
# chargeController(output1)
# batteryDC(output2)
