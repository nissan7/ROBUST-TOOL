from Tkinter import *
import tkMessageBox
import add_images as add_img
import login as l
import Tkinter, Tkconstants, tkFileDialog
import socket
import os


msgx=100
msgy=180
fmsgx=100
fmsgy=220
path=""
logged=0
fil1=open("info.txt","a+")
readed=fil1.read()

window=Tk()

def filename(path):
	fname=""
	for ch in path[::-1]:
		if ch=='/':
			break
		fname=ch+fname
	#print fname
	return fname

def getpath(event):
	global path
	path=tkFileDialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"),
					("text files","*.txt"),("pdf files","*.pdf"),("mp4 files","*.mp4")))	
	#print path

def upload(event):
	#print path
	s=socket.socket()
	


	
	if len(path)>0:
		s.connect(('127.0.0.1',4001))
		s.send("u")
		flag=s.recv(100)
		#print path
		name=filename(path)
		#print name
		s.send(name)
		dummy=s.recv(20)
		try:
			file=open(path,"r+b")
		except:
			pdf=Label(file_f,text="Unable to open file!\nCheck permission!",width=25,height=3)
			pdf.place(x=fmsgx,y=fmsgy)
			path=""
			return
			
		read=file.read(1024)
		while True:
			s.send(read)
			if (len(read)<=0):
				break
			read=file.read(1024)
		psf=Label(file_f,text="File uploaded",width=25,height=3)
		global path
		path=""
		psf.place(x=fmsgx,y=fmsgy)
		
	else:
		psf=Label(file_f,text="Please select file to upload",width=25,height=3)
		psf.place(x=fmsgx,y=fmsgy)
		#print "SELECT FILE"
	s.close()
	
	
def download(event):
	
	
	name=fil.get()
	if name!="":
		s=socket.socket()
		s.connect(('127.0.0.1',4001))
		s.send("d")
		dummy=s.recv(20)		
	
		#print len(name)
		#print name
		s.send(name)
		avail=s.recv(10)
		if avail=="1":
			s.send("1")
			#name=s.recv(20)
			f= open(name,"w")
			f.close()
			#s.send("send")
			
			while True:
				data=s.recv(1024)
				#print data
				f= open(name,"a+b")
				#print "recieving length"+str(len(data))
				f.write(data)
				f.close()
				
				if (len(data)<1024):
					#print "breaking"
					break
				
			psf=Label(file_f,text="FILE RECIEVED",width=25,height=3)
			psf.place(x=fmsgx,y=fmsgy)
		else:
			fnf=Label(file_f,text="FILE NOT FOUND",width=25,height=3)
			fnf.place(x=fmsgx,y=fmsgy)
	else:
		fsb=Label(file_f,text="Please fill search bar!",width=25,height=3)
		fsb.place(x=fmsgx,y=fmsgy)
	

	
	

def lclicked(event):
	clabel=Label(login_f,text="logged in",width=25,height=3)
	ilabel=Label(login_f,text="Well! that didn't work",width=25,height=3)
	dlabel=Label(login_f,text="Data limit reached!",width=25,height=3)
	slabel=Label(login_f,text="Connect to NIT Sikkim network\nSERVER DID NOT RESPOND",width=25,height=3)
	ulabel=Label(login_f,text="please provide user ID",width=25,height=3)
	plabel=Label(login_f,text="please provide password",width=25,height=3)
	userid=user.get()
	pasid=pas.get()
	
	if userid=='':
		ulabel.place(x=msgx,y=msgy)
		return
	if pasid=='':
		plabel.place(x=msgx,y=msgy)
		return
	
	
		
	stat=l.login(userid,pasid)   	#1-logged in
					#0-incorrect
					#3-data limit
					#2-connect to nit wifi
	result="no"	
	if stat==1:
		global logged
		logged=1
		clabel.place(x=msgx,y=msgy)
	elif stat==0:
		ilabel.place(x=msgx,y=msgy)
	elif stat==2:
		slabel.place(x=msgx,y=msgy)
	else:
		dlabel.place(x=msgx,y=msgy)
	global readed
	userinfo=readed.split('\n')
	if stat==1 and (userinfo[0]!=user.get() or userinfo[1]!=pas.get()):
		result = tkMessageBox.askquestion("FAST LOGIN", "Save this info for fast login ?\nprevious login info will be erased !", icon='info')
		
	if result=="yes" and stat==1:
			global fil1
			fil1.close()
			fil1=open("info.txt","w+")
			fil1.write(user.get()+"\n"+pas.get())			
			fil1.close()
			fil1=open("info.txt","r")
			readed=fil1.read()
			fil1.close()	


	

def fast_clicked(event):
	clabel=Label(login_f,text="fast logged in",width=25,height=3)
	ilabel=Label(login_f,text="Well! that didn't work\npassword is changed",width=25,height=3)
	flabel=Label(login_f,text="user info not added for\n Fast login \nlogin one time to save",width=25,height=3)
	slabel=Label(login_f,text="Connect to NIT Sikkim network\nSERVER DID NOT RESPOND",width=25,height=3)
	dlabel=Label(login_f,text="Data limit reached!",width=25,height=3)	
	if len(readed)==0:
		
		flabel.place(x=msgx,y=msgy)
	else:	
		userinfo=readed.split('\n')

		stat=l.login(userinfo[0],userinfo[1])
		if stat==1:
			global logged
			logged=1
			clabel.place(x=msgx,y=msgy)
		elif stat==0:
			ilabel.place(x=msgx,y=msgy)
		elif stat==2:
			slabel.place(x=msgx,y=msgy)
		else:
			dlabel.place(x=msgx,y=msgy)

def logout_clicked(event):
	logoutlabel=Label(login_f,text="LOGGED OUT",width=25,height=3)
	lflabel=Label(login_f,text="NOT LOGGED IN!",width=25,height=3)
	#dummyframe.grid(row=0,column=0,padx=2,pady=2,sticky=NW)
	#login_f.grid_forget()

	if logged==0:
		lflabel.place(x=msgx,y=msgy)
	else:
		logoutlabel.place(x=msgx,y=msgy)

def toggle_1(event):
	file_f.grid_forget()
	login_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
	
	
def toggle_2(event):
	login_f.grid_forget()
	file_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)

	

#add_img.app_logo(window)
window.title("ROBUST-TOOL")
window.geometry("410x320")
window.resizable(10,10)
nav_f=Frame(window,height=30,width=410,bg="#424c5e")
nav_f.grid(row=0,column=0)
toggle1=Button(nav_f,text="LOGIN")
toggle2=Button(nav_f,text="FILE_SHARING")
file_f=Frame(window,height=286,width=406,bg="#424c5e")
login_f=Frame(window,height=286,width=406,bg="#424c5e")
toggle1.bind('<Button-1>',toggle_1)
toggle2.bind('<Button-1>',toggle_2)
toggle1.place(x=2,y=2)
toggle2.place(x=73,y=2)

login_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
file_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)

userl=Label(login_f,text="USERNAME:")
user=Entry(login_f)
pasl=Label(login_f,text="PASSWORD:")
pas=Entry(login_f,show="*")

fast_login=Button(login_f,text="Fast Login")
fast_login.bind('<Button-1>',fast_clicked)

logout=Button(login_f,text="LOG-OUT")
logout.bind('<Button-1>',logout_clicked)

login=Button(login_f,text="login")
login.bind('<Button-1>',lclicked)

wlabel=Label(login_f,text="Welcome!",width=25,height=3)
wlabel.place(x=msgx,y=msgy)

userl.place(x=70,y=30)
user.place(x=160,y=30)

pasl.place(x=70,y=70)
pas.place(x=160,y=70)

logout.place(x=280,y=110)	
fast_login.place(x=40,y=110)
login.place(x=180,y=110)


#packing file sharing
fwlabel=Label(file_f,text="Welcome!",width=25,height=3)
fwlabel.place(x=fmsgx,y=fmsgy)

selectl=Button(file_f,text="SELECT FILE")
selectl.bind('<Button-1>',getpath)
selectl.place(x=30,y=20)

uploadl=Button(file_f,text="UPLOAD")
uploadl.bind('<Button-1>',upload)
uploadl.place(x=30,y=60)

fil=Entry(file_f)
fil.place(x=30,y=110)

downl=Button(file_f,text="DOWNLOAD")
downl.bind('<Button-1>',download)
downl.place(x=30,y=140)


window.mainloop()
