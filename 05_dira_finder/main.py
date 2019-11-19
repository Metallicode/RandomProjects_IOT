from application_manager import AppManager
from auto_dispatcher import Dispatcher

am = AppManager()
am.Setup()
ad = Dispatcher(am)
ad.StartDispatcher()
am.Start_TeleBot()
##ad.StopDispatcher()
