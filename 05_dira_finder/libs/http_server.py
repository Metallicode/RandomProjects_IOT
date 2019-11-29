import http.server
from urllib.parse import parse_qs
from libs.items_logger import Items_Logger
from libs.site_scrapper import SiteScrape
import json

class CORSRequestHandler (http.server.SimpleHTTPRequestHandler):
      items_logger = Items_Logger()
      def end_headers (self):          
            self.send_header('Access-Control-Allow-Origin', '*')
            http.server.SimpleHTTPRequestHandler.end_headers(self)

      def do_GET(self):
            print("get called..")
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            
            items = CORSRequestHandler.items_logger.Get_Favorite_Items()
            self.wfile.write(json.dumps(items).encode())

      def do_POST(self):
            length = int(self.headers.get('Content-length', 0))
            data = self.rfile.read(length).decode()
            message = ""
            item_id = ""
            try:
                  message = parse_qs(data)["message"][0]
            except:
                  item_id = parse_qs(data)["item_id"][0]

            if item_id == "":
                  CORSRequestHandler.items_logger.Log(message)
                  print(message, "sent to favorites")
            else:      
                  message = SiteScrape.Get_Phone_Number(item_id)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode())


