from site_scrapper import SiteScrape
import printer
from conf_reader import Get_Search_Data, Get_HTML_File_Location, Get_Bot_Key
import webbrowser
from tele_bot import TeleBot
import socketserver
from http_server import CORSRequestHandler
from threading import Thread 

class AppManager:
      def __init__(self, scrapehandler):
            self.HTMLFileLocation = Get_HTML_File_Location()
            self.bot = TeleBot(Get_Bot_Key())
            self.http_handler = CORSRequestHandler
            self.socket_server = socketserver.TCPServer(("", 8000), self.http_handler)
            SiteScrape.Set_Handler(scrapehandler)
            SiteScrape.Get_Old_Data_From_Disc()
            
      def Start_Http_Server(self):
            t = Thread(target=self.socket_server.serve_forever)
            t.start()
            
      def Start_TeleBot(self):
            self.bot.Listen()

      def Run(self):
            SiteScrape.SearchHandler.Create_Search_Url(Get_Search_Data())
            SiteScrape.Run()
            newData = SiteScrape.Get_New_Data()
            printer.Notify_Admin(newData)
            
            if len(newData)>0:
                  self.CreateHTML(open_browser=False)
                  self.bot.SendMessage(f"New Data! {len(newData)} new items!")
                  new_data_msg = self.bot.Prepare_News(SiteScrape.Get_New_Data())
                  self.bot.SendMessage(new_data_msg)
                  
      def PrintData(self):
            printer.Print_All_Data(SiteScrape.Get_Data())

      def GetPhoneNumber(self, id):
            return SiteScrape.Get_Phone_Number(id)
                  
      def CreateHTML(self, open_browser=True):
            printer.Make_HTML(SiteScrape.Get_New_Data_Buffer())
            if open_browser:
                  webbrowser.open(self.HTMLFileLocation)
                  
