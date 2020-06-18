
from socketserver import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr=self.request.getpeername()
        print('Got connection from',addr)
        meg='Thank you for connecting'
        self.wfile.write(meg.encode(encoding='utf_8'))

server=TCPServer(('',8899),Handler)
server.serve_forever()