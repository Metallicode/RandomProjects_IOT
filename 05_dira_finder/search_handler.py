from requests_html import HTMLSession

class SearchHandler:
      def __init__(self):
            self.new_data_buffer_max_size = 5
            self.new_data_buffer = []
            self.new_data = []
            self.old_data = []
            self.raw_data = None
            self.session = HTMLSession()
            self.url_base_str = ""
            self.url_str = ""
            self.id_api = ""

      def Create_Search_Url(self):
            pass

      def Get_Data_From_Web(self):
            if self.url_str != "":
                  print(f"Get_Data_From_Web {self.url_str}")
                  self.raw_data = self.session.get(self.url_str)

      def Get_Phone_Number(self, item_id):
            return "Get_Phone_Number not implemented..."

      def Push_To_NewDataBuffer(self, item):
            self.new_data_buffer.insert(0, item)
            if(len(self.new_data_buffer)>self.new_data_buffer_max_size):
                  self.new_data_buffer.pop()
                  
      def Handle_Data(self):
            return "Handle_Data not implemented..."

      def Get_New_Data(self):
            return self.new_data

      def Get_New_Data_Buffer(self):
            return self.new_data_buffer

      def Get_Data(self):
            return self.old_data



##############################Yad2##############################

import datetime
import json
from dira_item import Dira

class Yad2SearchHandler(SearchHandler):
      def __init__(self):
            super().__init__()
            self.url_base_str = "https://www.yad2.co.il/realestate/rent"
            self.id_api = "https://www.yad2.co.il/api/item/XXXXXX/contactinfo?id=1s0gw3&isPlatinum=true"
            self.city_dict = {"telaviv":"5000", "givatayim":"6300", "nesziona":"7200","rehovot":"8400","ramatgan":"8600","rishonlezion":"8300", "holon":"6600", "batyam":"6200", "petahtikva":"7900","ramathasharon":"2650", }

      def Get_Phone_Number(self, item_id):
            res = self.session.get(self.id_api.replace("XXXXXX",item_id))
            number = res.json()["data"]["phone_numbers"][0]["title"]
            name = res.json()["data"]["contact_name"]
            return f"{number} {name}"            

      def Create_Search_Url(self, search_data):
            self.url_str = f"{self.url_base_str}?city={self.city_dict[search_data['City']]}&rooms={search_data['Min_Rooms']}--1&price=-1-{search_data['Max_Price']}"        
            
      def Handle_Data(self):
            if self.raw_data is not None:
                  elements = self.raw_data.html.find('.feeditem')
                  data = []
                  self.new_data = []
     
                  for i in range(len(elements)):
                        item_id = list(elements[i].find(f'#feed_item_{i}')[0].attrs.keys())[1]
                        item_id = elements[i].find(f'#feed_item_{i}')[0].attrs[item_id]
                        
                        title = elements[i].find('.title')[0].text
                        subtitle = elements[i].find('.subtitle')[0].text
                        num_rooms = elements[i].find(f'#data_rooms_{i}')[0].text
                        square_meter = elements[i].find(f'#data_SquareMeter_{i}')[0].text
                        price = elements[i].find(f'#feed_item_{i}_price')[0].text
                        date = elements[i].find(f'.showDateInLobby')[0].text

                        if item_id is not "" and item_id != "true" and item_id != "false":
                              if len(price)>6:
                                    if price[6] == "₪":
                                          new_dira = Dira(item_id,title,subtitle,num_rooms,square_meter,price,date)
                                          data.append(new_dira)

                  data.sort(key=lambda r: r.date,reverse=True)

                  for i in data:
                        is_new_item = True
                        for j in self.old_data:
                              if i.item_id.strip() == j.item_id.strip():
                                    is_new_item = False
                                    break
                        if is_new_item is True:
                              self.old_data.append(i)
                              self.new_data.append(i)
                              self.Push_To_NewDataBuffer(i)
