from __future__ import absolute_import

from Plugins.Plugin import PluginDescriptor

from .YoutubeBrowser import YoutubeBrowser

def main(session, **kwargs):
	session.open(YoutubeBrowser)

def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Youtube"), description=_("Youtube"), where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU], fnc=main),
		]