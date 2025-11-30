from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHttpRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/logs":
            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)
            post_data_str = post_data_bytes.decode("utf-8")
            json_log = json.loads(post_data_str)
            print(json_log)
            self.send_response(200)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()