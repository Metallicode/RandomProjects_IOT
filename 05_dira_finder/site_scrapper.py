from requests_html import HTMLSession
import save_hebrew as sh
import datetime
import json

class SiteScrape:
      new_data_buffer = []
      old_data = sh.read_encoded_as_list()
      session = HTMLSession()
      url_str = ""
      id_api = ""
      raw_data = None

      @staticmethod
      def Set_Url(url, id_api):
            SiteScrape.url_str = url
            SiteScrape.id_api = id_api
            return url
      
      @staticmethod
      def Get_Phone_Number(item_id):
            res = SiteScrape.session.get(SiteScrape.id_api.replace("XXXXXX",item_id))
            number = res.json()["data"]["phone_numbers"][0]["title"]
            name = res.json()["data"]["contact_name"]
            return f"{number} {name}"

      @staticmethod
      def Run(url):
            SiteScrape.get_data_from_web()
            SiteScrape.handle_data()
            SiteScrape.Sync_To_Disc()

      @staticmethod
      def Get_Data():
            return SiteScrape.old_data

      @staticmethod
      def Get_New_Data():
            return SiteScrape.new_data_buffer     
            
      @staticmethod
      def get_data_from_web():
            SiteScrape.raw_data = SiteScrape.session.get(SiteScrape.url_str)
            
            
      @staticmethod
      def handle_data():
            if SiteScrape.raw_data is not None:
                  elements = SiteScrape.raw_data.html.find('.feeditem')
                  data = []
                  nl = '\n'
                  SiteScrape.new_data_buffer = []
     
                  for i in range(len(elements)):
                        item_id = list(elements[i].find(f'#feed_item_{i}')[0].attrs.keys())[1]
                        item_id = elements[i].find(f'#feed_item_{i}')[0].attrs[item_id]
                        
                        title = elements[i].find('.title')[0].text
                        subtitle = elements[i].find('.subtitle')[0].text
                        num_rooms = elements[i].find(f'#data_rooms_{i}')[0].text
                        square_meter = elements[i].find(f'#data_SquareMeter_{i}')[0].text
                        price = elements[i].find(f'#feed_item_{i}_price')[0].text
                        date = elements[i].find(f'.showDateInLobby')[0].text

                        if item_id is not "":
                              data_str = f'{item_id} {nl}{title} {nl}{subtitle} {nl}{num_rooms} {nl}{square_meter} {nl}{price} {nl}{date}'        
                              data.append((data_str, date))
                              
                  data.sort(key=lambda r: r[1],reverse=True)
                  data = [x[0] for x in data]
       
                  for i in data:
                        if i not in SiteScrape.old_data:
                              SiteScrape.old_data.append(i)
                              SiteScrape.new_data_buffer.append(i)

      @staticmethod
      def Sync_To_Disc():
            SiteScrape.old_data = sh.sync_data_to_file(SiteScrape.old_data)
                  
