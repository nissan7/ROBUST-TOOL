from Tkinter import *

def app_logo(window):
	logo=PhotoImage(file="logo.png")
	label=Label(window,image=logo)
	window.tk.call('wm', 'iconphoto', window._w, logo)
	label.grid()
