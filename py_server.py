import socket
HOST=''
PORT=8000

reply=b'Yes'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
print('LOG |||| listenning ')
s.listen(1)
conn,addr=s.accept()
print('LOG |||| Connected by ',addr,end='\n')
while True:
	request=conn.recv(1024).decode('UTF-8')
	if not request:break
	print('LOG |||| request is ',request,end='\n')
	conn.sendall(reply)
conn.close