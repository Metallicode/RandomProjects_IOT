import http.server
from urllib.parse import parse_qs
from libs.items_logger import Items_Logger

class CORSRequestHandler (http.server.SimpleHTTPRequestHandler):
      def end_headers (self):
            self.items_logger = Items_Logger()
            self.send_header('Access-Control-Allow-Origin', '*')
            http.server.SimpleHTTPRequestHandler.end_headers(self)

      def do_POST(self):
            length = int(self.headers.get('Content-length', 0))
            data = self.rfile.read(length).decode()
            message = parse_qs(data)["message"][0]

            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode())
            print(message, "sent to favorites")
            self.items_logger.Log(message)




