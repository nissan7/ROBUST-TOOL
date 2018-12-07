from Tkinter import *
import tkMessageBox
import add_images as add_img
import login as l
import Tkinter, Tkconstants, tkFileDialog
import socket
import os
import MySQLdb
from datetime import datetime
import secure as secure
class Calculator:	
    def __init__(self, master):
        self.master = master
        self.logged=0
        self.fil1=open("info.txt","a+")
        self.readed=self.fil1.read()
        self.msgx = 100
        self.msgy=180
	self.fmsgx=100
	self.fmsgy=230
	self.path=""
	self.msgx0=100
	self.msgy0=180
	self.userlogged=""
	self.mfflag=0
	
        master.title("ROBUST_TOOL")
        master.geometry("410x320")
        master.resizable(0,0)
	
	self.frame1=Frame(master,height=286,width=406,bg="green")
	self.frame1.grid(row=0,column=0)

        self.nav_f=Frame(self.frame1,height=30,width=410,bg="#424c5e")
        self.nav_f.grid(row=0,column=0) 
        self.toggle2=Button(self.nav_f,text="FILE_SHARING")
	self.logout=Button(self.nav_f,text="Logout")
        
        self.logout.bind('<Button-1>',self.toggle_10)
       
        self.toggle2.place(x=2,y=2)
	self.logout.place(x=330,y=2)
        
        
       
		
	self.addlogin0()
	self.encright=0
	#self.fil=Entry(self.file_f)
	#self.fil.place(x=30,y=110)
	
	#self.downl.place(x=30,y=140)
	
   	
    def addlogin0(self):
	self.frame1.grid_forget()
	self.frame0=Frame(self.master,height=286,width=406,bg="grey")
	self.frame0.grid(row=0,column=0)
	
	self.nav_f0=Frame(self.frame0,height=30,width=410,bg="#424c5e")
        self.nav_f0.grid(row=0,column=0,padx=0,pady=0)
	self.tool_f=Frame(self.frame0,height=286,width=406,bg="#424c5e")
	self.tool_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
       
        self.scaptive=Button(self.nav_f0,text="captive",command=self.toggle0lr)
	self.stool=Button(self.nav_f0,text="MY TOOL",command=self.toggle0rl)
	self.scaptive.place(x=2,y=2)
	self.stool.place(x=330,y=2)

	self.userl0=Label(self.tool_f,text="USERNAME:")
        self.userl0.place(x=70,y=30)
        self.user0=Entry(self.tool_f)
        self.user0.place(x=160,y=30)
        self.pasl0=Label(self.tool_f,text="PASSWORD:")
        self.pasl0.place(x=70,y=70)
        self.pas0=Entry(self.tool_f,show="*")
        self.pas0.place(x=160,y=70)	
	self.login0=Button(self.tool_f,text="login")
        self.login0.bind('<Button-1>',self.toggle_01)
        self.login0.place(x=180,y=110)
	wlabel0=Label(self.tool_f,text="Welcome!",width=25,height=3)
        wlabel0.place(x=self.msgx,y=self.msgy)
	self.addcaptive()
    def toggle0rl(self):
	self.login_f.grid_forget()
	self.tool_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
    def toggle0lr(self):
	self.tool_f.grid_forget()
	self.login_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)

    def addcaptive(self):
	self.login_f=Frame(self.frame0,height=286,width=406,bg="green")
	self.login_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
	self.userl=Label(self.login_f,text="USERNAME:")
        self.userl.place(x=70,y=30)
        self.user=Entry(self.login_f)
        self.user.place(x=160,y=30)
        self.pasl=Label(self.login_f,text="PASSWORD:")
        self.pasl.place(x=70,y=70)
        self.pas=Entry(self.login_f,show="*")
        self.pas.place(x=160,y=70)

        self.fast_login=Button(self.login_f,text="Fast Login")
        self.fast_login.place(x=40,y=110)
        self.fast_login.bind('<Button-1>',self.fast_clicked)
        self.login=Button(self.login_f,text="login")
        self.login.bind('<Button-1>',self.lclicked)
        self.login.place(x=180,y=110)
        self.logout=Button(self.login_f,text="LOG-OUT")
        self.logout.bind('<Button-1>',self.logout_clicked)
        self.logout.place(x=280,y=110)
        wlabel=Label(self.login_f,text="Welcome!",width=25,height=3)
        wlabel.place(x=self.msgx,y=self.msgy)
    def addfile(self):
	self.file_f=Frame(self.frame1,height=286,width=406,bg="#424c5e")
	self.file_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
	fwlabel=Label(self.file_f,text="Welcome!",width=25,height=3)
	fwlabel.place(x=self.fmsgx,y=self.fmsgy)
	self.tol=Label(self.file_f,text="upload for:")
	self.to=Entry(self.file_f)
	self.tol.place(x=10,y=10)
	self.to.place(x=100,y=10)
	self.selectl=Button(self.file_f,text="SELECT FILE")
	self.selectl.bind('<Button-1>',self.getpath)
	self.selectl.place(x=210,y=100)
	
	self.uploadl=Button(self.file_f,text="UPLOAD")
	self.uploadl.bind('<Button-1>',self.upload)
	self.uploadl.place(x=320,y=100)
	self.remarkl=Label(self.file_f,text="Remark:")
	self.remarkl.place(x=10,y=40)
	self.remarke=Entry(self.file_f,width=40)
	self.remarke.place(x=72,y=40)
	self.type = IntVar()
	self.type =0
	self.normal=Radiobutton(self.file_f, text="NORMAL", variable=self.type , value=0,command=self._0)
	self.sign=Radiobutton(self.file_f, text="SIGNED", variable=self.type , value=1,command=self._1)
	self.enc=Radiobutton(self.file_f, text="ENCIPTED",variable=self.type , value=2,command=self._2)
	self.signenc=Radiobutton(self.file_f, text="SIGNED AND ENCRIPTED",variable=self.type , value=3,command=self._3)
	self.normal.place(x=10,y=70)
	self.normal.select()
	self.sign.place(x=105,y=100)
	self.enc.place(x=10,y=100)
	self.signenc.place(x=115,y=70)
	#self.login_f.grid_forget()
	self.file_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
	self.c=self.db.cursor()
	sql="SELECT sender,file,remark,status,sign,new,date,size FROM file WHERE receiver=%s"
	self.c.execute(sql,(self.userlogged,))
	self.data=self.c.fetchall()
	self.c.close()
	self.db.commit()
	new=0
	for item in self.data:
		if item[5]==1:
			new=new+1
	count=Label(self.file_f,text=new)
	count.place(x=295,y=8)
	self.noti=Button(self.file_f,text="MY FILES",command=self.myfiles)
	self.noti.place(x=315,y=6)
	self.myfiles()
	
    def _0(self):
	self.type=0
    def _1(self):
	if self.encright==0:
		print "no sign"
		nas=Label(self.file_f,text="You are not Authorised to\n sign from this system",width=25,height=3)
		nas.place(x=self.fmsgx,y=self.fmsgy)
		return
	self.type=1
    def _2(self):
	if self.encright==0:
		nae=Label(self.file_f,text="You are not Authorised to\n encrypt from this system",width=25,height=3)
		nae.place(x=self.fmsgx,y=self.fmsgy)
		return
	self.type=2
    def _3(self):
	if self.encright==0:
		nase=Label(self.file_f,text="You are not Authorised to sign\n and encrypt from this system",width=25,height=3)
		nase.place(x=self.fmsgx,y=self.fmsgy)
		return
	self.type=3
    def logout_clicked(self,event):
    	logoutlabel=Label(self.login_f,text="LOGGED OUT",width=25,height=3)
    	lflabel=Label(self.login_f,text="NOT LOGGED IN!",width=25,height=3)
    	if self.logged==0:
    		lflabel.place(x=self.msgx,y=self.msgy)
    	else:
			logoutlabel.place(x=self.msgx,y=self.msgy)
    
    def fast_clicked(self, event):
		
	clabel=Label(self.login_f,text="fast logged in",width=25,height=3)
	ilabel=Label(self.login_f,text="Well! that didn't work\npassword is changed",width=25,height=3)
	flabel=Label(self.login_f,text="user info not added for\n Fast login \nlogin one time to save",width=25,height=3)
	slabel=Label(self.login_f,text="Connect to NIT Sikkim network\nSERVER DID NOT RESPOND",width=25,height=3)
	dlabel=Label(self.login_f,text="Data limit reached!",width=25,height=3)
		
	if len(self.readed)==0:
		flabel.place(x=self.msgx,y=self.msgy)
	else:	
		self.userinfo=self.readed.split('\n')
		self.stat=l.login(self.userinfo[0],self.userinfo[1])
		if self.stat==1:
			self.logged=1
			clabel.place(x=self.msgx,y=self.msgy)
		elif self.stat==0:
			ilabel.place(x=self.msgx,y=self.msgy)
		elif self.stat==2:
			slabel.place(x=self.msgx,y=self.msgy)
		else:
			dlabel.place(x=self.msgx,y=self.msgy)

    def lclicked(self,event):
		clabel=Label(self.login_f,text="logged in",width=25,height=3)
      	  	ilabel=Label(self.login_f,text="Well! that didnt work",width=25,height=3)
      		dlabel=Label(self.login_f,text="Data limit reached!\n or max login reached",width=25,height=3)
     		slabel=Label(self.login_f,text="Connect to NIT Sikkim network\nSERVER DID NOT RESPOND",width=25,height=3)
   		ulabel=Label(self.login_f,text="please provide user ID",width=25,height=3)
      		plabel=Label(self.login_f,text="please provide password",width=25,height=3)
		self.userid=self.user.get()
		self.pasid=self.pas.get()
		if self.userid=='':
			ulabel.place(x=self.msgx,y=self.msgy)
			return
		if self.pasid=='':
			plabel.place(x=self.msgx,y=self.msgy)
			return
		
		
			
		self.stat=l.login(self.userid,self.pasid)   	#1-logged in
						#0-incorrect
						#3-data limit
						#2-connect to nit wifi
		#print self.stat
		self.result="no"	
		if self.stat==1:
			self.logged=1
			clabel.place(x=self.msgx,y=self.msgy)
		elif self.stat==0:
			ilabel.place(x=self.msgx,y=self.msgy)
		elif self.stat==2:
			slabel.place(x=self.msgx,y=self.msgy)
		else:

			dlabel.place(x=self.msgx,y=self.msgy)
		
		self.userinfo=self.readed.split('\n')
		if self.stat==1 and (self.userinfo[0]!=self.user.get() or self.userinfo[1]!=self.pas.get()):
			self.result = tkMessageBox.askquestion("FAST LOGIN", "Save this info for fast login ?\nprevious login info will be erased !", icon='info')
			
		if self.result=="yes" and self.stat==1:
				self.fil1.close()
				self.fil1=open("info.txt","w+")
				self.fil1.write(self.user.get()+"\n"+self.pas.get())			
				self.fil1.close()
				self.fil1=open("info.txt","r")
				self.readed=self.fil1.read()
				self.fil1.close()

    #def toggle_2(self, event):
		
		
		
		
    def myfiles(self):
		if len(self.data)==0:
			return
		if self.mfflag==0:
			self.noti_f=Frame(self.file_f,height=90,width=305,bg="white")
			self.mfflag=1
			self.noti_f.place(x=50,y=135)
			self.index=0
			self.sender=[]
			self.files=[]
			self.remark=[]
			self.new=[]
			self.status=[]
			self.sign=[]
			self.sname=[]
			self.date=[]
			self.size=[]
			next=Button(self.file_f,text=">>")
			prev=Button(self.file_f,text="<<")
			next.bind('<Button-1>',self.next)
			prev.bind('<Button-1>',self.prev)
			self.remv=Button(self.file_f,text="REMOVE")
			self.downl=Button(self.file_f,text="DOWNLOAD")
			self.downl.bind('<Button-1>',self.download)
			self.downl.place(x=245,y=190)
			#self.remv.bind('<Button-1>',self.remove)
			for i in range (len(self.data)):
				#print self.data[i][0]
				self.sname.append(self.data[i][0])
				self.sender.append(Label(self.file_f,text=self.data[i][0]))
				self.files.append(Label(self.file_f,text=self.data[i][1]))
				self.remark.append(Label(self.file_f,text=self.data[i][2]))
				self.date.append(Label(self.file_f,text=self.data[i][6]))
				self.size.append(Label(self.file_f,text=str(self.data[i][7])+"bytes"))
				self.status.append(self.data[i][3])
				self.sign.append(self.data[i][4])
				self.new.append(self.data[i][5])
				
						
			
			next.place(x=355,y=170)
			prev.place(x=1,y=170)
			i=0	
			self.sender[self.index].place(x=55,y=140)
			self.files[self.index].place(x=130,y=140)
			self.remark[self.index].place(x=55,y=165)
			self.date[self.index].place(x=55,y=183)
			self.size[self.index].place(x=55,y=200)

			
				
		else:
			self.mfflag=0
			#self.noti_f.destroy()
    def next(self,event):
		if self.index<len(self.data)-1:
			self.sender[self.index].place_forget()
			self.files[self.index].place_forget()
			self.remark[self.index].place_forget()
			self.date[self.index].place_forget()
			self.size[self.index].place_forget()

			self.index+=1

			self.sender[self.index].place(x=55,y=140)
			self.files[self.index].place(x=130,y=140)
			self.remark[self.index].place(x=55,y=165)
			self.date[self.index].place(x=55,y=183)
			self.size[self.index].place(x=55,y=200)
    def prev(self,event):
		if self.index>0:
			self.sender[self.index].place_forget()
			self.files[self.index].place_forget()
			self.remark[self.index].place_forget()
			self.date[self.index].place_forget()
			self.size[self.index].place_forget()
			self.index-=1

			self.sender[self.index].place(x=55,y=140)
			self.files[self.index].place(x=130,y=140)
			self.remark[self.index].place(x=55,y=165)
			self.date[self.index].place(x=55,y=183)
			self.size[self.index].place(x=55,y=200)
		
		


    def toggle_1(self, event):

		self.file_f.grid_forget()
		self.login_f.grid(row=1,column=0,padx=2,pady=2,sticky=NW)
    def filename(self):
		fname=""
		for ch in self.path[::-1]:
			if ch=='/':
				break
			fname=ch+fname
		#print fname
		return fname
    def getpath(self,event):
		self.path=tkFileDialog.askopenfilename(initialdir = "/home	",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"),("text files","*.txt"),("pdf files","*.pdf"),("mp4 files","*.mp4")))	
	#print path

    def upload(self,event):
		#print path
		if self.to.get()=="" or self.path=="":
			pmt=Label(self.file_f,text="Please mention receiver\n and select file path",width=25,height=3)
			pmt.place(x=self.fmsgx,y=self.fmsgy)
			return
		signature=None
		#to=self.to.get()
		#print str(self.type)+"type" 
		if self.type ==2 or self.type==3:
			#print "encrypted"
			self.c.close()
			self.c=self.db.cursor()
			sql="SELECT public FROM user WHERE userid=%s"
			self.c.execute(sql,(self.to.get(),))
			data=self.c.fetchall()
			self.c.close()
			self.db.commit()
			print data
			secure.encryptFile(self.path,data[0][0])
			self.path=self.path+".enc"
		if self.type==1 or self.type==3:
			signature=secure.signf(self.path)
			print (signature)
			
		name=self.filename()
		s=socket.socket()
		if len(self.path)>0:
			s.connect(('127.0.0.1',4001))
			s.send("u")
			flag=s.recv(100)
			filesize=os.path.getsize(self.path)
			
			#print path
			#name=self.filename()
			#print name
			s.send(name)
			dummy=s.recv(20)
			try:
				file=open(self.path,"r+b")
			except:
				pdf=Label(self.file_f,text="Unable to open file!\nCheck permission!",width=25,height=3)
				pdf.place(x=self.fmsgx,y=self.fmsgy)
				self.path=""
				return
				
			read=file.read(1024)
			while True:
				s.send(read)
				if (len(read)<=0):
					break
				read=file.read(1024)
			now = datetime.now()
			formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
			self.c=self.db.cursor()
			sql = "INSERT INTO file (sender,file,receiver,remark,size,date,status,sign,new) VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s)"
			val = (self.userlogged,name, self.to.get(),self.remarke.get(),filesize,formatted_date,self.type,signature,1)
			self.c.execute(sql,val)
			psf=Label(self.file_f,text="File uploaded",width=25,height=3)
			
			psf.place(x=self.fmsgx,y=self.fmsgy)
			self.c.close()
			self.db.commit()
			
			if self.type==2 or self.type==3:			
				os.remove(self.path)
				print "deleting"+str(self.path)
			self.path=""
			
			
			
		else:	
			psf=Label(self.file_f,text="Please select file to upload",width=25,height=3)
			psf.place(x=self.fmsgx,y=self.fmsgy)
			#print "SELECT FILE"
		s.close()

    def toggle_01(self,event):
		
		self.db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="PRACTICE")
		self.c=self.db.cursor()
		self.userlogged=self.user0.get()
		pass0=self.pas0.get()
		sql="SELECT userid,password FROM user WHERE userid=%s"
		self.c.execute(sql,(self.userlogged,))
		data=self.c.fetchall()
		self.c.close()
		self.db.commit()
		if len(data)==0:
			unr=Label(self.tool_f,text="USER NOT REGISTERED!",width=25,height=3)
			unr.place(x=self.msgx0,y=self.msgy0)
			return
		if data[0][1]==pass0:
			
			self.frame0.grid_forget()
			self.frame1.grid(row=0,column=0)
			self.addfile()
			#self.addcaptive()
			self.frame0.destroy()
			self.c=self.db.cursor()
			sql="SELECT public FROM user WHERE userid=%s"
			self.c.execute(sql,(self.userlogged,))
			data=self.c.fetchall()
			self.c.close()
			self.db.commit()
			if data[0][0]==None:
				if os.path.isfile("./"+"PublicKey.pem"):
					self.encright=0
				else:			
					secure.keygen()
					fp=open("PublicKey.pem","r")
					keyp=fp.read()
					fp.close()
					print keyp+str(len(keyp))
					self.c=self.db.cursor()
					sql="UPDATE user SET public = %s WHERE userid = %s"
					self.c.execute(sql,(keyp,self.userlogged,))
					self.c.close()
					self.db.commit()
					self.encright=1			
			else:
				if os.path.isfile("./"+"PublicKey.pem"):
					fp=open("PublicKey.pem","r")
					keyp=fp.read()
					fp.close()
					if keyp==data[0][0]:
						print "matched"
						self.encright=1
					else:
						print "unmatched"
						self.encright=0;
						
				else:
					self.encright=0
				
			"""try:
       				 = open(prompt, 'r').readlines()
    			except FileNotFoundError:
       				print("Wrong file or file path")"""
		else:
			pi=Label(self.tool_f,text="PASSWORD INCORRECT!",width=25,height=3)
			pi.place(x=self.msgx0,y=self.msgy0)
			

		
    def toggle_10(self,event):
		
		self.addlogin0()
		#self.login_f.destroy()
		self.file_f.destroy()
		#self.noti_f.destroy()
		self.frame1.grid_forget()
		self.encright=0
		
    def download(self,event):
		name=self.data[self.index][1]
		if name!="":
			s=socket.socket()
			try:
				s.connect(('127.0.0.1',4001))
			except:
				snr=Label(self.file_f,text="SERVER IS NOT RESPONDING",width=25,height=3)
				snr.place(x=self.fmsgx,y=self.fmsgy)
				f_path=""
				return
				
			s.send("d")
			dummy=s.recv(20)		
			
			#print len(name)
			#print name
			s.send(name)
			filesize=s.recv(20)
			print filesize
			s.send("d")
			avail=s.recv(10)
			if avail=="1":
				f_path=tkFileDialog.askdirectory(initialdir = "/")
				
				#print f_path
				s.send("1")
				#name=s.recv(20)
				f= open(f_path+"/"+name,"w")
				f.close()
				#s.send("send")
				
				while True:
					data=s.recv(1024)
					#print data
					f= open(f_path+"/"+name,"a+b")
					#print "recieving length"+str(len(data))
					f.write(data)
					f.close()
					
					if (len(data)<1024):
						#print "breaking"
						break
					
				psf=Label(self.file_f,text="FILE RECIEVED",width=25,height=3)
				psf.place(x=self.fmsgx,y=self.fmsgy)
				if self.status[self.index]==1 or self.status[self.index]==3:
					print self.sname[self.index]
					print type(self.sname[self.index])
					self.c=self.db.cursor()
					sql="SELECT public FROM user WHERE userid=%s"
					self.c.execute(sql,(str(self.sname[self.index]),))
					key=self.c.fetchall()
					self.c.close()
					self.db.commit()
					print key
					if secure.verifyf(f_path+"/"+name,key[0][0],self.sign[self.index]):
						tkMessageBox.showinfo("SIGNATURE VERIFICATION", "FILE IS AUTHENTIC!")
					else:
						tkMessageBox.showinfo("SIGNATURE VERIFICATION", "FILE HAS BEEN TEMPERED\nPLEASE DISCARD FILE!")

					
				if self.status[self.index]==2 or self.status[self.index]==3:
					print "path hai"+str(f_path+"/"+name)
					secure.decryptFile(f_path+"/"+name)
					
					os.remove(f_path+"/"+name)
				
			else:
				fnf=Label(self.file_f,text="FILE NOT FOUND",width=25,height=3)
				fnf.place(x=self.fmsgx,y=self.fmsgy)

		
	




root = Tk()
my_gui = Calculator(root)
root.mainloop()
