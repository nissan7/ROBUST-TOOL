import mechanize
from bs4 import BeautifulSoup
def login(user,pas):	
	br=mechanize.Browser()
	br.set_handle_robots(False)
	br.add_header=[('User','Firefox')]
	try:	
		res=br.open("http://172.16.32.1:8090")
	except: 
		return 2 #wifi is not connected to COLLEGE NETWORK
	br.select_form(nr=0)
	br.form['username']=user
	br.form['password']=pas
	res=br.submit()
	html=res.read()
	soup=BeautifulSoup(html,"html5lib")
	item=soup.find('message')
	msg=item.string
	#print msg
	if msg[7]=='T':
		return 0
	elif msg[10]==' ':
		return 1
	else:
		return 2
#1-logged in
#0-incorrect
#3-data limit
#2-connect to nit wifi
