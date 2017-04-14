import serial
from serial import SerialException
import os
from BatteryController import BatteryController
from ChargeController import ChargeController

#Make sure to change this depending on your system, this one is for mac
#linux will be something like "ttyUSB0"
#windows will be something like "COM1"
#the baud rate should be 19200

ser = serial.Serial("/dev/tty.usbmodem1421", 19200)




#main loop
#output = "02,3,00,00,00,037,000,00,02,000,00,483,0000,00,032"


while 1:
	output =ser.readline()
	if(len(output)>3):
		if(output[3]=='5'):
			deviceType="Inverter"
			print(output)
			#inverterData(deviceType, output)
		if(output[3]=='3'):
			print(output)
			deviceType="Charge Controller"
			cc=ChargeController()
			cc.chargeControl(array=output,deviceType=deviceType)
		if(output[3]=='4'):
			print(output)
			deviceType="DC Battrey Monitor"
			#bC= BatteryController()
			bc= BatteryController()
			bc.batteryDC(deviceType=deviceType, array=output)
			#print(output, deviceType)

#this is for testing purposes (do not remove)
#output = "02,3,00,00,00,037,000,00,02,000,00,483,0000,00,032"
# output = "03,4,0014,0001,0000,01,00000,482,100,110,08,99,057"
# chargeController(output1)
# batteryDC(output2)
