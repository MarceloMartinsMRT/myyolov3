# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import urllib.parse
import os
import wget
import urllib.request

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        print("testeeeee "+self.path)

        message = "Hello, World!"
        workkickup = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query).get('workkickup', None)
        print(workkickup)  # Prints None or the string value of workkickup


        cmd1 = 'python workkickup.py '
        '''

        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        url=''
        local='testeeee.mp4'
        urllib.request.urlretrieve(workkickup[0],local)

'''
        if(workkickup != None):
            os.system(cmd1 + workkickup[0])


    

        self.wfile.write(bytes(message + str(self.path), "utf8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")





