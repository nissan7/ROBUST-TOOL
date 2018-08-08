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
	clabel=Label(window,text="logged in",width=25,height=3)
	ilabel=Label(window,text="Well! that didn't work",width=25,height=3)
	dlabel=Label(window,text="Data limit reached!",width=25,height=3)
	slabel=Label(window,text="Connect to NIT Sikkim network\nSERVER DID NOT RESPOND",width=25,height=3)
	ulabel=Label(window,text="please provide user ID",width=25,height=3)
	plabel=Label(window,text="please provide password",width=25,height=3)
	userid=user.get()
	pasid=pas.get()
	
	if userid=='':
		ulabel.place(x=msgx,y=msgy)
		return
	if pasid=='':
		plabel.place(x=msgx,y=msgy)
		return
	
	
		
	stat=l.login(userid,pasid)
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
	if stat==1 and (userinfo[0]!=user.get()):
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
	clabel=Label(window,text="fast logged in",width=25,height=3)
	
	flabel=Label(window,text="user info not added for\n Fast login \nlogin one time to save",width=25,height=3)
	slabel=Label(window,text="Connect to NIT Sikkim network\nSERVER DID NOT RESPOND",width=25,height=3)
	dlabel=Label(window,text="Data limit reached!",width=25,height=3)	
	if len(readed)==0:
		
		flabel.place(x=msgx,y=msgy)
	else:	
		userinfo=readed.split('\n')

		stat=l.login(userinfo[0],userinfo[1])
		if stat==1:
			global logged
			logged=1
			clabel.place(x=msgx,y=msgy)
		elif stat==2:
			slabel.place(x=msgx,y=msgy)
		else:
			dlabel.place(x=msgx,y=msgy)

def logout_clicked(event):
	logoutlabel=Label(window,text="LOGGED OUT",width=25,height=3)
	lflabel=Label(window,text="NOT LOGGED IN!",width=25,height=3)
	if logged==0:
		lflabel.place(x=msgx,y=msgy)
	else:
		logoutlabel.place(x=msgx,y=msgy)



add_img.app_logo(window)
window.title("ROBUST-TOOL")
window.geometry("400x300")
window.resizable(10,10)
mainframe=Frame(window,height=296,width=396,bg="#424c5e")
mainframe.grid(row=0,column=0,padx=2,pady=2,sticky=NW)

userl=Label(mainframe,text="USERNAME:")
user=Entry(mainframe)
pasl=Label(mainframe,text="PASSWORD:")
pas=Entry(mainframe,show="*")

fast_login=Button(mainframe,text="Fast Login")
fast_login.bind('<Button-1>',fast_clicked)

logout=Button(mainframe,text="LOG-OUT")
logout.bind('<Button-1>',logout_clicked)

login=Button(mainframe,text="login")
login.bind('<Button-1>',lclicked)

wlabel=Label(window,text="Welcome!",width=25,height=3)
wlabel.place(x=msgx,y=msgy)

userl.place(x=70,y=30)
user.place(x=160,y=30)

pasl.place(x=70,y=70)
pas.place(x=160,y=70)

logout.place(x=280,y=110)	
fast_login.place(x=40,y=110)
login.place(x=180,y=110)

window.mainloop()
