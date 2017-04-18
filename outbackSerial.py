import serial
<<<<<<< HEAD
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
=======

#Make sure to change this depending on your system, this one is for mac
#linux will be something like "ttyUSB0"
#windows will be something like "COM1"
#the baud rate should be 19200

ser = serial.Serial("/dev/tty.usbmodem1411", 19200)


#formats the bits for battery to the correct values
def batteryDC(array, deviceType):
	shuntACurrent =array[5:8]+"."+array[8:9]
	shuntBCurrent = array[10:13]+"."+array[13:14]
	shuntCCurrent = array[15:18]+"."+array[18:19]
	extraDataIdentifier = array[20:22]
	extraData = array[23:28]
	batteryVoltage = array[29:31]+"."+array[31:32]
	stateOfCharge = array[33:36]
	enableFlagShunt = array[37:40]
	statusFlag = array[41:43]
	batteryTemp = array[44:46]
	checkSum = array[47:50]
	print deviceType
	print "Shunt A current:"+shuntACurrent + ", Shunt B Current:"+shuntBCurrent+", Shunt C Current:"+shuntCCurrent
	print "Extra Data Identifier:"+extraDataIdentifier +",Extra Data:"+extraData
	print "Battery Voltage:"+ batteryVoltage+ ", State Of charge:"+ stateOfCharge+"%"+", enable Flag A,B,C:"+enableFlagShunt
	print "Status Flag High|Low:"+statusFlag +", Battery Temperature:"+batteryTemp+"C" + ", Check Sum:"+checkSum

#formats the bits for chargeController to the correct value
def chargeController(array, deviceType):
	chargeCurrrent = array[8:10]
	pvCurrent = array[11:13]
	pvVoltage = array[14:17]
	dailyKillowattshour = array[18:21]
	chargeCurrentLengths = array[22:24]
	auxMode = array[25:27]
	errorCodes = array[28:31]
	chargeMode = array[32:34]
	batteryVoltage = array[35:37]+"."+array[37:38]
	dailyAMPhours = array[39:43]
	checkSum = array[47:50]
	print deviceType
	print "charge Current:" + chargeCurrrent + ", pvCurrent:" +pvCurrent + ", PV voltage"+ pvVoltage
	print "dailyKillowatts-hour:"+dailyKillowattshour + ", charge current length:" + chargeCurrentLengths
	print "daily AUX mode:" + auxMode + ", Error Codes:" + errorCodes +", Charge Mode:" + chargeMode
	print "Battrey Voltage:" + batteryVoltage+ ", daily AMP Hours:" + dailyAMPhours + ", Check sum:" + checkSum

#main loop
while 1:
	output =ser.readline()
	if(outback[3]=='5'):
		deviceType="Inverter"
		print output
		#inverterData(deviceType, output)
	elif(outback[3]=='3'):
		deviceType="Charge Controller"
		chargeController(output, deviceType)
	elif(outback[3]=='4'):
		deviceType="DC Battrey Monitor"
	print(output, deviceType)

#this is for testing purposes (do not remove)
# output1 = "02,3,00,00,00,037,000,00,02,000,00,483,0000,00,032"
# output2 = "03,4,0014,0001,0000,01,00000,482,100,110,08,99,057"
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
# chargeController(output1)
# batteryDC(output2)
