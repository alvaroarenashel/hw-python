import http.server
import socketserver
from functools import partial

from http.server import BaseHTTPRequestHandler, HTTPServer

class MessageStorage:
    def __init_(self,newValue=""):
        self.value = newValue
    
    def set(self, newValue):
        self.value = newValue

    def get(self):
        return self.value
    

class SimpleHandler(BaseHTTPRequestHandler):
    # msg = MessageStorage()
    def __init__(self, message, *args, **kwargs):
        self.msg = message
        super().__init__(*args,**kwargs)
        # print("SimpleHandler init with msg="+ self.msg.get())

    def _set_response(self,http_status=200):
        self.send_response(http_status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("Current msg is >"+ self.msg.get() + "<")
        self._set_response()
        self.wfile.write(self.msg.get().encode('utf-8'))

    def do_POST(self):
        print("Processing POST")
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        responseMessage = ""

        if(content_length < 100):
            self.msg.set(post_data.decode('utf-8'))
            responseMessage = "Message updated to >" + self.msg.get() + "<"
            print(responseMessage)
            self._set_response()
        else:
            responseMessage = "Body to long. Will not set a new message >.<"
            print(responseMessage)
            self._set_response(400)

        self.wfile.write(responseMessage.encode('utf-8'))

def run(server_class=HTTPServer, port=8080):
    storage = MessageStorage()
    storage.set("Hola")
    handler = partial(SimpleHandler, storage)
    server_address = ('', port)
    httpd = server_class(server_address, handler)
    httpd.serve_forever()    

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
