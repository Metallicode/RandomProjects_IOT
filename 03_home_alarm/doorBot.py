from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import serial
import threading
import time

USER_PASS = "pass"
messageCounter = 0
kill_thread = False
s = serial.Serial('COM5',9600)

def job(bot, update):
      global kill_thread
      global messageCounter
      s.reset_input_buffer()
      print("job started!")
      while True:
            if s.inWaiting()>0:
                  doorstate = s.readline().decode()
                  if(doorstate == "DOOR OPEN\r\n"):
                        messageCounter += 1
                        if(messageCounter < 5):
                              bot.send_message(chat_id=update.message.chat_id, text="ALERT!!!  DOOR OPEN!!!")
                              time.sleep(2)
            else:
                  messageCounter=0
            if(kill_thread):
                  messageCounter = 0
                  break
      print("job is dead...")

def lockDoor(bot, update, args):
      global kill_thread

      if(args[0] == USER_PASS):     
            kill_thread = False
            t = threading.Thread(target=job, args=(bot, update))
            t.start()
            bot.send_message(chat_id=update.message.chat_id, text="DOORBOT ACTIVE")

def openDoor(bot, update, args):
      global kill_thread
      if(args[0] == USER_PASS):
            kill_thread = True
            bot.send_message(chat_id=update.message.chat_id, text="DOOR IS OPEN")      

def start(bot, update):
      bot.send_message(chat_id=update.message.chat_id, text="I AM DOORBOT")

updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('open', openDoor, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('lock', lockDoor, pass_args=True))

print("DOORBOT STARTING")
updater.start_polling()
updater.idle()









