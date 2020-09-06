import kivy
from kivy.app import App
from kivy.uix.label import Label

from jnius import autoclass, cast
from android.broadcast import BroadcastReceiver
from android.permissions import Permission , request_permissions


class B_receiver:
	def __init__(self):
		
		self.broadCastReceiver()
		

	request_permissions([Permission.ACCESS_WIFI_STATE, Permission.CHANGE_WIFI_STATE])
	Context = autoclass('android.content.Context')
	Intent = autoclass('android.content.Intent')
	IntentFilter = autoclass('android.content.IntentFilter')
   
	PythonActivity = autoclass('org.kivy.android.PythonActivity')
	activity = PythonActivity.mActivity
	wifi_manager = cast('android.net.wifi.WifiManager',activity.getSystemService(Context.WIFI_SERVICE))

	def broadCastReceiver(self):
		print('Iam in broadcastreceiver')
		self.br = BroadcastReceiver(self.onReceive, actions= None,categories=None)
		self.br.start()

	def onReceive(self,context,intent):
		print('Iam in onreceive')
		success = intent.getBooleanExtra(wifi_manager.EXTRA_RESULTS_UPDATED,false)
		if(success):
			self.scanSuccess()
			self.br.stop()
		else:
			self.scanFailure()
			self.br.stop()
	c = Context()
	intent_filter = IntentFilter()
	intent_filter.addAction(wifi_manager.SCAN_RESULTS_AVAILABLE_ACTION)
	c.registerReceiver(self.br,intent_filter)
	success = wifi_Manager.startScan()
	if not success:

		self.scanFailure()

	def scanSuccess(self):
		results = wifi_manager.getScanResults()
		print(results)

	def scanFailure(self):

		results = wifi_manager.getScanResults()

class MyApp(App):

    def build(self):
    	
        self.b_r = B_receiver()
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
