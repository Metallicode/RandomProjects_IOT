import time
import datetime
from threading import Thread
from random import randrange

class Dispatcher:
      def __init__(self,manager, interval=60):
            self.manager = manager
            self.active = False
            self.interval = interval
            self.t = None
            
      def StopDispatcher(self):
            self.active = False
     
      def StartDispatcher(self):
            self.t = Thread(target=self.DispatcherLoop)
            self.active = True
            self.t.start()

      def DispatcherLoop(self):
            while self.active:
                  self.Job()
                  time.sleep(self.GetRandomInterval()) 

      def Job(self):
            print(f">>dispatcher calls manager.Run() at {datetime.datetime.now()}")
            self.manager.Run()

      def GetRandomInterval(self):
            return randrange(self.interval, self.interval+10)
