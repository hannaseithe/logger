from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from .db import save_log


class MyHttpRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/logs":
            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)
            post_data_str = post_data_bytes.decode("utf-8")
            json_log = json.loads(post_data_str)
            json_log["ip"] = self.client_address[0]  # IP-Adresse des Clients
            save_log(json_log)
            self.send_response(200)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()