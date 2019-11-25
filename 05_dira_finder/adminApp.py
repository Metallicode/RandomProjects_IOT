from site_scrapper import SiteScrape
import printer
import os
from conf_reader import Get_Search_Data
import webbrowser
import search_handler

if __name__ == "__main__":
      os.system('cls')
      handler = search_handler.Yad2SearchHandler()
      SiteScrape.Set_Handler(handler)
      SiteScrape.Sync_To_Disc()
           
      while True:
            user_selection = input("1 - run query \n2 - print data \n3 - get phone number\n4 - make HTML\n5 - quit\n")
            if user_selection == "1":
                  SiteScrape.SearchHandler.Create_Search_Url(Get_Search_Data())
                  SiteScrape.Run() 
                  printer.Notify_Admin(SiteScrape.Get_New_Data())
                  input()
            elif user_selection == "2":
                  os.system('cls')     
                  printer.Print_All_Data(SiteScrape.Get_Data())
                  input()
            elif user_selection == "3":
                  idNum = input("enter item id:\n")
                  print(SiteScrape.Get_Phone_Number(idNum))
                  input()
            elif user_selection == "4":
                  printer.Make_HTML(SiteScrape.Get_Data())
                  print("html created\n")
                  url = "file://C:/Users/grysd/Desktop/dira/view_data.html"
                  webbrowser.open(url)
            elif user_selection == "5":
                  exit()
            else:
                  print("waaat?\n")

            os.system('cls')
            
