from Tkinter import *
import tkMessageBox
import add_images as add_img
import login as l



msgx=100
msgy=180
logged=0
fil=open("info.txt","a+")
readed=fil.read()

window=Tk()

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
			global fil
			fil.close()
			fil=open("info.txt","w+")
			fil.write(user.get()+"\n"+pas.get())			
			fil.close()
			fil=open("info.txt","r")
			readed=fil.read()
			fil.close()	


	

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

window.mainloop()
