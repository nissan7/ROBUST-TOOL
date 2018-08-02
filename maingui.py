from Tkinter import *
import add_images as add_img
import login as l
msgx=100
msgy=180
window=Tk()
def fast_clicked(event):
	flabel=Label(window,text="NOT AVAILABLE!",width=25,height=3)
	flabel.place(x=msgx,y=msgy)
def lclicked(event):
	clabel=Label(window,text="logged in",width=25,height=3)
	ilabel=Label(window,text="Well! that didn't work",width=25,height=3)
	ulabel=Label(window,text="please provide user ID",width=25,height=3)
	plabel=Label(window,text="please provide password",width=25,height=3)
	dlabel=Label(window,text="Data limit reached!",width=25,height=3)
	userid=user.get()
	pasid=pas.get()
	if userid=='':
		ulabel.place(x=msgx,y=msgy)
		return
	if pasid=='':
		plabel.place(x=msgx,y=msgy)
		return
		
		
	stat=l.login(userid,pasid)
	if stat==1:
		clabel.place(x=msgx,y=msgy)
	elif stat==0:
		ilabel.place(x=msgx,y=msgy)
	else:
		dlabel.place(x=msgx,y=msgy)

add_img.app_logo(window)
window.title("ROBUST-TOOL")
window.geometry("400x300")
window.resizable(10,10)
mainframe=Frame(window,height=296,width=396,bg="#424c5e")
mainframe.grid(row=0,column=0,padx=2,pady=2,sticky=NW)

user=Entry(mainframe)
pas=Entry(mainframe,show="*")
login=Button(mainframe,text="login")
fast_login=Button(mainframe,text="Fast Login")
#pas.place(x=0,y=0)
fast_login.bind('<Button-1>',fast_clicked)
login.bind('<Button-1>',lclicked)
userl=Label(mainframe,text="USERNAME:")
pasl=Label(mainframe,text="PASSWORD:")
wlabel=Label(window,text="Welcome!",width=25,height=3)

userl.place(x=70,y=30)
user.place(x=160,y=30)

pasl.place(x=70,y=70)
pas.place(x=160,y=70)

fast_login.place(x=100,y=110)
login.place(x=250,y=110)

wlabel.place(x=msgx,y=msgy)

window.mainloop()
