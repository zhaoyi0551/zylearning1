from socketserver import TCPServer,StreamRequestHandler,ForkingMixIn

class Server(ForkingMixIn,TCPServer):pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr=self.request.getpeername()
        print('Got connection from',addr)
        meg='Thank you for connecting'
        self.wfile.write(meg.encode(encoding='utf_8'))

server=TCPServer(('',1234),Handler)
server.serve_forever()