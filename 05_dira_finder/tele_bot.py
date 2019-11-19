from telegram.ext import Updater, CommandHandler

class TeleBot:
      def __init__(self, telegram_key):
            self.subscribers = []
            self.updater = Updater(telegram_key)
            self.updater.dispatcher.add_handler(CommandHandler('start', self.Start))
            self.updater.dispatcher.add_handler(CommandHandler('subscribe', self.Subscribe))

      def Listen(self):
            self.updater.start_polling()
            self.updater.idle()


      def Start(self, bot, update):
            self.bot = bot

      def Subscribe(self, bot, update):
            print(update.message.chat_id)
            self.subscribers.append(update.message.chat_id)
            self.bot.send_message(chat_id=update.message.chat_id, text="You are Subscribed!")

      def SendMessage(self, msg):
            for subscriber in self.subscribers:
                  self.bot.send_message(chat_id=subscriber, text=msg)
