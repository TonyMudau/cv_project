import http.server 
import socketserver
import os 

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/summary.png':
            self.path ='/summary.png'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8080

handler = myhandler
print("Server started at PORT"+str(PORT))
myserver = socketserver.TCPServer(("", PORT), handler)
myserver.serve_forever()

