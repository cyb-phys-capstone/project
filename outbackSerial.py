import serial
from serial import SerialException
import datetime
from ChargeController import ChargeController
from BatteryController import BatteryController
import psycopg2
from random import randint

# Make sure to change this depending on your system, this one is for mac
# linux will be something like "ttyAMA0/ACM0"
# windows will be something like "COM1"
# the baud rate should be 19200

ser = serial.Serial("/dev/tty.usbmodem1421", 19200)

dt =datetime.datetime.now()
chargeID=randint(1, 1000000)
batteryID=randint(1, 10000000)

# main loop
output = "02,3,00,00,00,037,000,00,02,000,00,483,0000,00,032"


def insertBattery():
	query = """INSERT INTO home_bdata (id, current_soc, current_kw, current_kvar, state, capacity, roundtrip_eff,
	min_soc, max_charging_rate, max_discharging_rate, charging_eff, discharging_eff, required_reserve, rated_voltage,
	phase, current_voltage, b_id_id, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
	return query
def insertCharge():
	query = """INSERT INTO home_sdata (id, output_voltage, current, real_power, s_id_id, timestamp) VALUES (%s, %s, %s, %s, %s, %s);"""
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
# cursor.execute("select column_name from information_schema.columns where table_name='home_nodecontroller'")
# column_names = [row[0] for row in cursor]
# print (column_names)
# cursor.execute("""SELECT * FROM home_nodecontroller""")
# print(cursor.fetchall())
# print (dt)


while 1:
	output =ser.readline()
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
			deviceType="DC Battrey Monitor"
			bc= BatteryController()
			bc.batteryDC(deviceType=deviceType, array=output)
			print(bc.shuntAKillo)
			cursor.execute(insertBattery(),(batteryID, bc.stateOfCharge, bc.shuntAKillo,12, 2.0, 24.0, 90.0, bc.minSOC, 1.0, 1.0, bc.netInputAH, bc.netOutputAH, 20.0, 24.0, 1, bc.batteryVoltage, 1, dt))
			conn.commit()
			#print(output, deviceType)

# this is for testing purposes (do not remove)
# output = "02,3,00,00,00,037,000,00,02,000,00,483,0000,00,032"
# output = "03,4,0014,0001,0000,01,00000,482,100,110,08,99,057"
# chargeController(output1)
# batteryDC(output2)
