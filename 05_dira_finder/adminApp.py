from site_scrapper import SiteScrape
import printer
import os
from conf_reader import Get_Search_Url, Get_API_Str
import webbrowser

url_str = Get_Search_Url()
id_api = Get_API_Str()

if __name__ == "__main__":
      os.system('cls')
      SiteScrape.Sync_To_Disc()
      SiteScrape.Set_Url(url_str, id_api)

      while True:
            user_selection = input("1 - run query \n2 - print data \n3 - get phone number\n4 - make HTML\n5 - quit\n")
            if user_selection == "1":
                  SiteScrape.Run(url_str)
                  printer.Notify_User(SiteScrape.Get_New_Data())
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
            
