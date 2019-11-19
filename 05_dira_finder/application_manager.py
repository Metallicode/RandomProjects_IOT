from site_scrapper import SiteScrape
import printer
from conf_reader import Get_Search_Url, Get_API_Str, Get_HTML_File_Location, Get_Bot_Key
import webbrowser
from tele_bot import TeleBot

class AppManager:
      def __init__(self):
            self.url_str = Get_Search_Url()
            self.id_api = Get_API_Str()
            self.HTMLFileLocation = Get_HTML_File_Location()
            self.bot = TeleBot(Get_Bot_Key())

      def Setup(self):
            SiteScrape.Set_Url(self.url_str, self.id_api)
            SiteScrape.Sync_To_Disc()
            
      def Start_TeleBot(self):
            self.bot.Listen()

      def Run(self):
            SiteScrape.Run(self.url_str)
            newData = SiteScrape.Get_New_Data()
            printer.Notify_User(newData)
            
            if len(newData)>0:
                  self.CreateHTML(open_browser=False)
                  self.bot.SendMessage(f"New Data! {len(newData)} new items!")
                  
      def PrintData(self):
            printer.Print_All_Data(SiteScrape.Get_Data())

      def GetPhoneNumber(self, id):
            return SiteScrape.Get_Phone_Number(id)
                  
      def CreateHTML(self, open_browser=True):
            printer.Make_HTML(SiteScrape.Get_Data())
            if open_browser:
                  webbrowser.open(self.HTMLFileLocation)
                  
