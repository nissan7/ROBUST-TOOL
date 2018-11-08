import socket
s=socket.socket()
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

s.connect(('172.16.3.71',4002))


s.send("u")


flag=s.recv(100)
if flag=="ok":
	name=raw_input("enter file name")
	path=find(name,"./")
	if path!=None:
		s.send(name)
		dummy=s.recv(20)
		file=open(path,"r+b")
		read=file.read(1024)
		while True:
			s.send(read)
			if (len(read)<=0):
				break
			read=file.read(1024)
		print "sent"
		
	else:
		print"file not found"
