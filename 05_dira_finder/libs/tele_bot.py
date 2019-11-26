from telegram.ext import Updater, CommandHandler, RegexHandler
from libs.site_scrapper import SiteScrape
from threading import Thread
from libs.conf_reader import Set_Config

class TeleBot:
      def __init__(self, telegram_key):
            self.updater = Updater(telegram_key)
            self.updater.dispatcher.add_handler(CommandHandler('start', self.Start))
            self.updater.dispatcher.add_handler(CommandHandler('mute', self.Mute))
            self.updater.dispatcher.add_handler(CommandHandler('news', self.GetNews))
            self.updater.dispatcher.add_handler(CommandHandler('set', self.Set, pass_args=True))
            self.updater.dispatcher.add_handler(CommandHandler('subscribe', self.Subscribe))
            self.updater.dispatcher.add_handler(RegexHandler('^(/d_[\w]+)$', self.GetInfo))
            self.subscribers = []
            self.bot = self.updater.bot

            with open("libs/telebot_subscribers.txt", "r") as f:
                  for i in f.readlines():
                        if i:
                              i = i.split(',')
                              subscriber = {"subscriber_id":int(i[0]), "mute":i[1]}
                              self.subscribers.append(subscriber)

      def Set(self, bot, update, args):
            ok_words = ["city", "max_price", "min_rooms"]
            message = "OK"
            if args[0].lower() in ok_words:
                  Set_Config(args[0].lower(), args[1].lower())
            else:
                  message = "Problem With Args.."
            
            self.bot.send_message(chat_id=update.message.chat_id, text=f"{message} {args}")
            

      def Mute(self, bot, update):
            for i in self.subscribers:
                  if i["subscriber_id"] == update.message.chat_id:
                        i["mute"] = not i["mute"]
                        self.bot.send_message(chat_id=update.message.chat_id, text=f"mute is {i['mute']}")
                        self.Save_To_File()
                
      def GetInfo(self, bot, update):
            info_id = update.message.text.replace('/d_', '')
            info = SiteScrape.Get_Phone_Number(info_id)
            clickable = f"+972{info.split()[0][1:].replace('-','')}"
            self.bot.send_message(chat_id=update.message.chat_id, text=f"{info.split()[1]} \n{clickable}")
            
      def Listen(self):
            self.updater.start_polling()
            self.updater.idle()

      def Start(self, bot, update):
            print("start")
            pass

      def Save_To_File(self):
            with open("libs/telebot_subscribers.txt", "w") as f:
                  for i in range(len(self.subscribers)):
                        new_str = f"{self.subscribers[i]['subscriber_id']},{self.subscribers[i]['mute']}"
                        if i != len(self.subscribers)-1:
                              new_str=new_str+"\n"
                        f.write(new_str)
                  
      def Subscribe(self, bot, update):
            print(update.message.chat_id)
            if update.message.chat_id not in self.subscribers:
                  self.bot.send_message(chat_id=update.message.chat_id, text="OK! your chat id is Subscribed")
                  new_subscriber = {"subscriber_id":update.message.chat_id,"mute":False}
                  self.subscribers.append(new_subscriber)
                  t = Thread(target=self.Save_To_File)
                  t.start()              
            else:
                  self.bot.send_message(chat_id=update.message.chat_id, text="You are Subscribed!")

      def GetNews(self, bot, update):
            news = self.Prepare_News(SiteScrape.Get_New_Data_Buffer())
            self.bot.send_message(chat_id=update.message.chat_id, text=news)
                  
      def Prepare_News(self, new_data):     
            max_items = SiteScrape.SearchHandler.new_data_buffer_max_size
            if len(new_data) < max_items:
                  message_to_user = ""
                  max_items = len(new_data)
            message_to_user = f"\n**TOP {max_items}**\n"
            for i in range(max_items):
                  message_to_user += "/d_"+new_data[i].Get_String()
                  message_to_user += "\n>>>>>>>>>>\n"
            return message_to_user
                  
      def SendMessage(self, msg):
            for subscriber in self.subscribers:
                  if subscriber["mute"] is False:
                        self.bot.send_message(chat_id=subscriber["subscriber_id"], text=msg)
