from site_scrapper import SiteScrape
import printer
from conf_reader import Get_Search_Url, Get_API_Str, Get_HTML_File_Location, Get_Bot_Key
import webbrowser
from tele_bot import TeleBot
import search_handler

class AppManager:
      def __init__(self):
            self.HTMLFileLocation = Get_HTML_File_Location()
            self.bot = TeleBot(Get_Bot_Key())

      def Setup(self):
            SiteScrape.Set_Handler(search_handler.Yad2SearchHandler(Get_Search_Url(),Get_API_Str()))
            SiteScrape.Get_Old_Data_From_Disc()
            
      def Start_TeleBot(self):
            self.bot.Listen()

      def Run(self):
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
            printer.Make_HTML(SiteScrape.Get_New_Data())
            if open_browser:
                  webbrowser.open(self.HTMLFileLocation)
                  
