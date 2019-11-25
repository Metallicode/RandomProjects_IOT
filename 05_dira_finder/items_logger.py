from save_hebrew import save_to_favorite

class Items_Logger:
      def Log(self, data):
            save_to_favorite(self.Parse_Data(data))

      def Parse_Data(self, data):
            return data+"\n"

