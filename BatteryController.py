from decimal import Decimal
class BatteryController():
	shuntACurrent = None
	shuntBCurrent = None
	shuntCCurrent = None
	shuntAAmpHrs = None
	shuntBAmpHrs = None
	shuntCAmpHrs = None
	shuntAKillo = None
	shuntBKillo = None
	shuntCKillo = None
	daysSinceFull = None
	minSOC = None
	netInputAH = None
	netOutputAH = None
	netInputKWH = None
	netOutputKWH = None
	netBatteryAHCF = None
	netBatteryKWHCF = None
	batteryVoltage = None
	stateOfCharge = None
	flagShuntStatusA= None
	flagShuntStatusB = None
	flagShuntStatusC = None
	relayMode = None
	relayState = None
	status = None
	temperatureBattery = None
	RTS = None
	systemStatus = None
	NA = False



	def batteryDC(self, deviceType, array):
		aCurrent =array[5:8]+"."+array[8:9]
		bCurrent = array[10:13]+"."+array[13:14]
		cCurrent = array[15:18]+"."+array[18:19]
		self.shuntCurrentFunc(currentA=aCurrent, currentB=bCurrent, currentC=cCurrent)
		extraDataIdentifier = array[20:22]
		extraData = array[23:28]
		self.extraDataIdentifierFunc(extraDataIdentifierValues=extraDataIdentifier, extraDataValues=extraData)

		voltage = array[29:32]
		self.batteryVoltageFunc(voltage=voltage)
		chargeState = array[33:36]

		enableFlagShuntA = array[37:38]
		enableFlagShuntB = array[38:39]
		enableFlagShuntC = array[39:40]
		self.flagShuntFunc(flagA=enableFlagShuntA, flagB=enableFlagShuntB, flagC=enableFlagShuntC)

		statusFlag = array[41:43]
		self.statusFlagFunc(status=statusFlag)
		batteryTemp = array[44:46]
		self.batteryTempFunc(batteryTemp=batteryTemp)
		checkSum = array[47:50]
		self.checkSumFunc(checkSum=checkSum, output=array)

	def shuntCurrentFunc(self, currentA, currentB, currentC):
		self.shuntACurrent = (Decimal("".join(currentA))) / 10
		self.shuntBCurrent = (Decimal("".join(currentB))) / 10
		self.shuntCCurrent = (Decimal("".join(currentC))) / 10

	def extraDataIdentifierFunc(self, extraDataIdentifierValues, extraDataValues):
		identifier = int("".join(extraDataIdentifierValues))
		extraData = "".join(extraDataValues)
		if(identifier==0):
			self.shuntAAmpHrs = int(extraData)
		elif(identifier==1):
			self.shuntAKillo = (Decimal(extraData))/100
		elif(identifier==2):
			self.shuntBAmpHrs = int(extraData)
		elif(identifier==3):
			self.shuntBKillo = (Decimal(extraData))/100
		elif (identifier==4):
			self.shuntCAmpHrs = int(extraData)
		elif (identifier==5):
			self.shuntCKillo = (Decimal(extraData))/100
		elif(identifier==6):
			self.daysSinceFull = (Decimal(extraData))/10
		elif(identifier==7):
			self.minSOC = int(extraData)
		elif(identifier==8):
			self.netInputAH = int(extraData)
		elif(identifier==9):
			self.netOutputAH = int(extraData)
		elif(identifier==10):
			self.netInputKWH = (Decimal(extraData))/100
		elif(identifier==11):
			self.netOutputKWH = (Decimal(extraData))/100
		elif(identifier==12):
			self.netBatteryAHCF = int(extraData)
		elif(identifier==13):
			self.netBatteryKWHCF = (Decimal(extraData))/100
		else:
			self.NA = True

	def batteryVoltageFunc(self, voltage):
		self.batteryVoltage = (Decimal("".join(voltage))) / 10

	def stateChargeFunc(self, chargeState):
		self.stateOfCharge = int("".join(chargeState))

	def flagShuntFunc(self, flagA, flagB, flagC):
		flagA = int("".join(flagA))
		flagB = int("".join(flagB))
		flagC = int("".join(flagC))
		if(flagA ==1):
			self.flagShuntStatusA = True
		else:
			self.flagShuntStatusA = False
		if (flagB == 1):
			self.flagShuntStatusB = True
		else:
			self.flagShuntStatusB = False
		if (flagC == 1):
			self.flagShuntStatusC = True
		else:
			self.flagShuntStatusC = False
	def statusFlagFunc(self, status):
		status = int("".join(status))
		if(status == 1):
			"value"
		elif(status == 2):
			self.relayMode = True
		elif(status == 4):
			self.relayState == True
	def batteryTempFunc(self, batteryTemp):
		self.temperatureBattery = int("".join(batteryTemp))
		if(self.temperatureBattery == 99):
			self.RTS = True
	def checkSumFunc(self, output, checkSum):
		checkSum= int("".join(checkSum))
		output="".join(output)
		output= output.replace(",","")
		output = list(output)
		output=output[:-3]
		output = int("".join(output))
		if(output==checkSum):
			self.systemStatus = True




