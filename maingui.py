from Tkinter import *
import add_images as add_img
import login as l

window=Tk()

def lclicked(event):
	userid=user.get()
	pasid=pas.get()
	l.login(userid,pasid)

add_img.app_logo(window)
window.title("ROBUST-TOOL")
window.geometry("400x300")
window.resizable(10,10)
mainframe=Frame(window,height=296,width=396,bg="#424c5e")
mainframe.grid(row=0,column=0,padx=2,pady=2,sticky=NW)

user=Entry(mainframe)
pas=Entry(mainframe)
login=Button(mainframe,text="login")
fast_login=Button(mainframe,text="Fast Login")
#pas.place(x=0,y=0)
login.bind('<Button-1>',lclicked)
userl=Label(mainframe,text="USERNAME:")
pasl=Label(mainframe,text="PASSWORD:")


userl.place(x=70,y=30)
user.place(x=160,y=30)

pasl.place(x=70,y=70)
pas.place(x=160,y=70)

fast_login.place(x=100,y=110)
login.place(x=250,y=110)


window.mainloop()
