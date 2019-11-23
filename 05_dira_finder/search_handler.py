from requests_html import HTMLSession

class SearchHandler:
      def __init__(self, url_str, id_api):
            self.new_data_buffer_max_size = 5
            self.new_data_buffer = []
            self.new_data = []
            self.old_data = []
            self.raw_data = None
            self.session = HTMLSession()
            self.url_str = url_str
            self.id_api = id_api

      def Get_Data_From_Web(self):
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
      def __init__(self, url_str, id_api):
            super().__init__(url_str, id_api)

      def Get_Phone_Number(self, item_id):
            res = self.session.get(self.id_api.replace("XXXXXX",item_id))
            number = res.json()["data"]["phone_numbers"][0]["title"]
            name = res.json()["data"]["contact_name"]
            return f"{number} {name}"            

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
