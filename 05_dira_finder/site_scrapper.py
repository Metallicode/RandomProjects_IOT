import save_hebrew as sh

class SiteScrape:

      SearchHandler = None

      @staticmethod
      def Set_Handler(SearchHandler):
            SiteScrape.SearchHandler = SearchHandler
      
      @staticmethod
      def Get_Phone_Number(item_id):
            return SiteScrape.SearchHandler.Get_Phone_Number(item_id)

      @staticmethod
      def Run():
            SiteScrape.SearchHandler.Get_Data_From_Web()
            SiteScrape.SearchHandler.Handle_Data()
            SiteScrape.Sync_To_Disc()

      @staticmethod
      def Get_Data():
            return SiteScrape.SearchHandler.old_data

      @staticmethod
      def Get_New_Data():
            return SiteScrape.SearchHandler.new_data     

      @staticmethod
      def Get_New_Data_Buffer():
            return SiteScrape.SearchHandler.new_data_buffer    
            
      @staticmethod
      def get_data_from_web():
            SiteScrape.SearchHandler.Get_Data_From_Web()
              
      @staticmethod
      def handle_data():
            SiteScrape.SearchHandler.Handle_Data()
       
      @staticmethod
      def Sync_To_Disc():
            SiteScrape.SearchHandler.old_data = sh.sync_data_to_file(SiteScrape.SearchHandler.old_data)
                  
      @staticmethod
      def Get_Old_Data_From_Disc():
            SiteScrape.SearchHandler.old_data = sh.read_encoded_as_list()
