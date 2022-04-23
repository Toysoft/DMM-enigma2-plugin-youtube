from enigma import eConsoleAppContainer, eDBoxLCD, eRCInput, fbClass
from Components.Language import language
from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen
from Tools.Log import Log

from twisted.internet import reactor

class YoutubeBrowser(Screen, ServiceStopScreen):#
	skin = """<screen name="YoutubeBrowser" position="0,0" size="100%,100%" background="#000000" flags="wfNoBorder"></screen>"""
	def __init__(self, session):
		Screen.__init__(self, session, windowTitle="YouTube")
		ServiceStopScreen.__init__(self)

		self.__container = eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.__container_conn = self.__container.dataAvail.connect(self.__consoleData)
		self.stopService()
		self.onFirstExecBegin.append(self.__run)

	def __run(self):
		#eDBoxLCD.getInstance().lock()
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		cmd = "export LANG=" + language.getLanguage() + ".UTF-8;/usr/bin/dreamium"
		Log.w(cmd)
		reactor.callLater(3, self.__container.execute, cmd)

	def __consoleData(self, data):
		Log.i(data)

	def __runFinished(self, retval=1):
		#Log.w(retval)
		#eDBoxLCD.getInstance().unlock()
		eRCInput.getInstance().unlock()
		fbClass.getInstance().unlock()
		self.close()
