import socket

HOST='172.16.150.49'
PORT=8000

request=b'my requset info'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('LOG |||| start connetting')
s.connect((HOST,PORT))

s.sendall(request)
reply=s.recv(1024)
print('LOG |||| reply is ',reply.decode('UTF-8'))
s.close