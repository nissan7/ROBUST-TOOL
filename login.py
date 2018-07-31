import mechanize
def login(user,pas):	
	br=mechanize.Browser()
	br.set_handle_robots(False)
	br.add_header=[('User','Firefox')]
	res=br.open("http://172.16.32.1:8090")
	br.select_form(nr=0)
	br.form['username']=user
	br.form['password']=pas
	res=br.submit()
	print res
