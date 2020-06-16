import socket
s=socket.socket()

host=socket.gethostname()
port=1250
s.bind((host,port))

s.listen(5)
while True:

    c,addr=s.accept()
    print('Got connection from ',addr)
    meg='thank you for connection!'
    c.sendall(meg.encode(encoding='utf_8'))
    c.close()
