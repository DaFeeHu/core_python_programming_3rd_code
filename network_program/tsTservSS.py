#!/usr/bin/env python
from socketserver import TCPServer, StreamRequestHandler
from time import ctime

HOST = ''
PORT = 23535
ADDR = (HOST, PORT)


class MyRequestHander(StreamRequestHandler):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(
            bytes('%s %s' % (ctime(), self.rfile.readline()), 'utf-8'))


tcpServ = TCPServer(ADDR, MyRequestHander)
print('waiting for connection...')
tcpServ.serve_forever()
