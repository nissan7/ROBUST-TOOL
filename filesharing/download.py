import socket
s=socket.socket()
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

s.connect(('127.0.0.1',4001))

s.send("d")
			

print "coming"
name=raw_input("enter file name")
s.send(name)
avail=s.recv(10)
if avail=="1":
	s.send("1")
	#name=s.recv(20)
	f= open("11"+name,"w")
	f.close()
	#s.send("send")
	
	while True:
		data=s.recv(1024)
		f= open("1"+name,"a+b")
		#print "recieving length"+str(len(data))
		f.write(data)
		f.close()
		
		if (len(data)<1024):
			#print "breaking"
			break
		
	print "recieved"
else:
	print "file not found"
	

