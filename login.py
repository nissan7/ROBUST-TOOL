import mechanize
user=raw_input("Enter username")
print user
pas=raw_input("Enter password\n")
print pas
br=mechanize.Browser()
br.set_handle_robots(False)
br.add_header=[('User','Firefox')]
res=br.open("http://172.16.32.1:8090")
print res
br.select_form(nr=0)
br.form['username']=user
br.form['password']=pas
res=br.submit()
print res
