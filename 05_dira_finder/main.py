from libs.application_manager import AppManager
from libs.auto_dispatcher import Dispatcher
from  libs.search_handler import Yad2SearchHandler

am = AppManager(Yad2SearchHandler())
ad = Dispatcher(am)
ad.StartDispatcher()
am.Start_Http_Server()
am.Start_TeleBot()
