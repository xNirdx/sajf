import socketserver
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')

host = config['NET']['HOST']
port = int(config['NET']['PORT'])


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = json.loads(self.request.recv(1024).strip())

        if self.data['type'] == 'message':
            # the packet recieved contains a message
            pass


with socketserver.TCPServer((host, port), MyTCPHandler) as server:
    server.serve_forever()
