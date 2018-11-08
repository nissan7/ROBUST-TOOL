import socket
import thread
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def communication(c):
	service=c.recv(20)

	if service=="u":
		c.send("ok")
		name=c.recv(20)
		if name!="":
			f= open(name,"w")
			f.close()
		c.send("send")
		
		while True:
			data=c.recv(1024)
			f= open(name,"a+b")
			f.write(data)
			f.close()
			if (len(data)<=0):
				print "recieved"
				break
		
						
	if service=="d":
		print "coming"
		c.send("ok")
		name=c.recv(100)
		print "request for:"+name
		path=find(name,"./")
		if path!=None:
			c.send("1")
			dummy=c.recv(10)
			#c.send(name)
			file=open(path,"r+b")
			read=file.read(1024)
			while True:
				#print "sending length:"+str(len(read))
				c.send(read)
				if (len(read)<=0):
					break
				read=file.read(1024)
			print "sent"
		else:
			c.send("0")
		
		


s=socket.socket()
s.bind(('127.0.0.1',4001))
print 'Server started!'
print 'Waiting for clients...'

s.listen(1)

while True:
	c,addr=s.accept()
	print "connected with"+str(c)
	thread.start_new_thread(communication,(c,))
s.close()	
