import socket
HOST=''
PORT=8000

reply='Yes'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(3)
print('LOG |||| listenning ')
coon,addr=s.accept()

request=conn.recv(1024)

print('LOG |||| request is ',request,end='\n')
print('LOG |||| Connected by ',addr,end='\n')
conn.sendall(reply)
conn.close