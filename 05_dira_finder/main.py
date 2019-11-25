from application_manager import AppManager
from auto_dispatcher import Dispatcher
import search_handler

am = AppManager(search_handler.Yad2SearchHandler())
ad = Dispatcher(am)
ad.StartDispatcher()
am.Start_Http_Server()
am.Start_TeleBot()
