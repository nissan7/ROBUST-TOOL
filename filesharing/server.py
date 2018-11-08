
    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()

import socket

def Main():




"""
	try:
		data=c.recv(1024)
	except:
		print "connection lost"
	while str(data)!="q":
		print "request for:"+data
		
		try:
			path=find(data,"./")
			print path
			if path!=None:
				size=os.path.getsize(path)
				c.send("yes")
				dummy=c.recv(1024)
				
				print size
				c.send(str(size))
				download=c.recv(1024)
				if download=="y":
					print "user wants to download"
					file=open(path,"r+b")
					read=file.read(1024)
					while(len(read)>0):
						#print "reading"+read
						c.send(read)
						read=file.read(1024)
					print "file sent"
						
						
				else:
					print "no downloading"
			else:
				c.send("no")
		except:
			print "connection lost"
			break
		try:
			data=c.recv(1024)
		except:
			print "connection lost"
			break
	return
	
"""		

