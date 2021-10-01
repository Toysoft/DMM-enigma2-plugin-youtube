from enigma import eConsoleAppContainer, eDBoxLCD, eRCInput, fbClass
from Components.Language import language
from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen
from Tools.Log import Log

class YoutubeBrowser(Screen, ServiceStopScreen):
	def __init__(self, session):
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)

		self.__container = eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__run()

	def __run(self):
		#eDBoxLCD.getInstance().lock()
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		cmd = "export LANG=" + language.getLanguage() + ".UTF-8;/usr/bin/dreamium"
		Log.w(cmd)
		self.__container.execute(cmd)


	def __runFinished(self, retval=1):
		#Log.w(retval)
		#eDBoxLCD.getInstance().unlock()
		eRCInput.getInstance().unlock()
		fbClass.getInstance().unlock()
		self.close()
