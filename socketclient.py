import socket

s=socket.socket()

host=socket.gethostname()
port=8899

s.connect((host,port))
print(s.recv(1024).decode(encoding='utf_8'))