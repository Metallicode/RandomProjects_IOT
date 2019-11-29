from libs.save_hebrew import save_to_favorite, read_favorite_items

class Items_Logger:
      def __init__(self):
            self.favorite_items = read_favorite_items()
      
      def Log(self, data):
            save_item = True
            data_dict = eval(data)
            for i in self.favorite_items:
                  if i["item_id"] == data_dict["item_id"]:
                        save_item = False
                        print("item is already in favorite_items")
                        break
            if save_item is True:
                  self.favorite_items.append(data_dict)
                  save_to_favorite(self.Parse_Data(data))

      def Parse_Data(self, data):
            return data+"\n"

      def Get_Favorite_Items(self):
            return self.favorite_items
