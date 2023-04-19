from enigma import eConsoleAppContainer, eSystemResourceLock
from Components.Label import Label
from Components.Language import language
from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen
from Tools.Log import Log

from twisted.internet import reactor

class YoutubeBrowser(Screen, ServiceStopScreen):#
	skin = """<screen name="YoutubeBrowser" position="0,0" size="100%,100%" backgroundColor="#000000" flags="wfNoBorder">
		<widget name="state" position="0,0" size="100%,100%" halign="center" valign="center" foregroundColor="#FFFFFF" backgroundColor="#000000" font="Regular;128"/>
	</screen>"""
	def __init__(self, session):
		Screen.__init__(self, session, windowTitle="YouTube")
		ServiceStopScreen.__init__(self)

		self["state"] = Label(_("Loading YouTube ..."))
		self.__container = eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.__container_conn = self.__container.dataAvail.connect(self.__consoleData)
		self.stopService()
		self._shouldRun = True
		self._lock = None
		self.onShown.append(self.__run)

	def __run(self):
		if not self._shouldRun:
			return
		self._shouldRun = False
		self._lock = eSystemResourceLock()
		reactor.callLater(.5, self.__doRun)

	def __doRun(self):
		cmd = "export LANG=" + language.getLanguage() + ".UTF-8;/usr/bin/dreamium"
		Log.w(cmd)
		reactor.callLater(2, self.__container.execute, cmd)

	def __consoleData(self, data):
		Log.i(data)

	def __runFinished(self, retval=1):
		self._lock = None
		self.close()
