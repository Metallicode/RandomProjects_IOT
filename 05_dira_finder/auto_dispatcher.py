import time
import datetime
from threading import Thread

class Dispatcher:
      def __init__(self,manager, interval=60):
            self.manager = manager
            self.active = False
            self.interval = interval
            self.t = Thread(target=self.DispatcherLoop)
            
      def StopDispatcher(self):
            self.active = False
     
      def StartDispatcher(self):
            self.active = True
            self.t.start()

      def DispatcherLoop(self):
            while self.active:
                  self.job()
                  time.sleep(self.interval) 

      def job(self):
            print(f">>dispatcher calls manager.Run() at {datetime.datetime.now()}")
            self.manager.Run()
            
