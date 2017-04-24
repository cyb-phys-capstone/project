from decimal import Decimal
class ChargeController():
	chargeCurrent = None
	pvCurrent = None
	pvVoltage = None
	dailyKWH = None
	chargeCurrentLengths= None
	auxMode = None
	faultCode = None
	chargeMode = None
	batteryVoltage = None
	dailAH = None
	systemStatus = None
	warning = None

	
	def chargeControl(self, array, deviceType):
		chargeCurrrent = array[8:10]
		self.chargeCurrentFunc(chargeCurrent=chargeCurrrent)

		pvCurrent = array[11:13]
		self.pvCurrentFunc(pvCurrent=pvCurrent)

		pvVoltage = array[14:17]
		self.pvVoltageFunc(pvVoltage=pvVoltage)

		dailyKillowattshour = array[18:21]
		self.dailyKWHFunc(dailyKWH=dailyKillowattshour)

		chargeCurrentLengths = array[22:24]
		self.chargeCurrentLengthsFunc(chargeCurrentLengths=chargeCurrentLengths)

		auxMode = array[25:27]
		self.auxModeFunc(auxMode=auxMode)

		errorCodes = array[28:31]
		self.faultCodesFunc(faultCode=errorCodes)

		chargeMode = array[32:34]
		self.chargeModeFunc(chargeMode=chargeMode)

		batteryVoltage = array[35:38]
		self.batteryVoltageFunc(batteryVoltage=batteryVoltage)

		dailyAMPhours = array[39:42]
		self.dailyAHFunc(dailyAH=dailyAMPhours)

		checkSum = array[47:50]
		self.checkSumFunc(checkSum=checkSum, output=array)

		print (self.pvVoltage)

	def chargeCurrentFunc(self,chargeCurrent):
		self.chargeCurrent= int("".join(chargeCurrent))

	def pvCurrentFunc(self, pvCurrent):
		self.pvCurrent = int("".join(pvCurrent))

	def pvVoltageFunc(self, pvVoltage):
		self.pvVoltage = int("".join(pvVoltage))

	def dailyKWHFunc(self, dailyKWH):
		self.dailyKWH = int("".join(dailyKWH))

	def chargeCurrentLengthsFunc(self, chargeCurrentLengths):
		self.chargeCurrentLengths = (Decimal("".join(chargeCurrentLengths))) / 10

	def auxModeFunc(self, auxMode):
		auxMode = int("".join(auxMode))
		if(auxMode == 0):
			self.auxMode = "Disabled"
		elif(auxMode == 1):
			self.auxMode = "Diversion"
		elif(auxMode == 2):
			self.auxMode = "Remote"
		elif(auxMode == 3):
			self.auxMode = "Manual"
		elif(auxMode == 4):
			self.auxMode = "Vent Fan"
		elif(auxMode == 5):
			self.auxMode = "PV Trigger"
		elif(auxMode == 6):
			self.auxMode = "Float"
		elif(auxMode == 7):
			self.auxMode = "Fault Outout"
		elif(auxMode == 8):
			self.auxMode = "Night Light"
		elif(auxMode == 9):
			self.auxMode = "PWM Diversion"
		elif(auxMode == 10):
			self.auxMode == "Low Battery"

	def faultCodesFunc(self, faultCode):
		faultCode = int("".join(faultCode))
		if(faultCode >= 1 | faultCode <= 16):
			self.faultCode = "Unused"
		elif(faultCode == 32):
			self.faultCode = "Shorted Battery Sensor"
		elif(faultCode == 64):
			self.faultCode == "Too Hot"
		elif(faultCode == 128):
			self.faultCode = "High VOC"

	def chargeModeFunc(self, chargeMode):
		chargeMode = int("".join(chargeMode))

		if(chargeMode == 0):
			self.chargeMode = "Silent"
		elif(chargeMode == 1):
			self.chargeMode = "Float"
		elif(chargeMode == 2):
			self.chargeMode = "Bulk"
		elif(chargeMode == 3):
			self.chargeMode = "Absorb"
		elif(chargeMode == 4):
			self.chargeMode = "Equalize"

	def batteryVoltageFunc(self, batteryVoltage):
		self.batteryVoltage = (Decimal("".join(batteryVoltage))) / 10

	def dailyAHFunc(self, dailyAH):
		self.dailAH = int("".join(dailyAH))

	def checkSumFunc(self, output, checkSum):
		checkSum= int("".join(checkSum))
		output="".join(output)
		output= output.replace(",","")
		output = list(output)
		output=output[:-3]
		output = int("".join(output))
		if(output==checkSum):
			self.systemStatus = True

