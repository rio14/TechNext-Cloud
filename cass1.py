#!/usr/bin/python2

import cgitb,cgi,commands,random

print "Contant-type:text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
n=x.getvalue("num")
u=x.getvalue('uname')
p=x.getvalue('pas')

port=random.randint(6000,7000)
commands.getoutput("sudo systemctl restart docker")
print "<html>"
print "access your container using links:"
print "<br>"
print "</html>"
for i in range(int(n)) :
	commands.getoutput("sudo docker run -it -p "+ str(port) +":4200  -d   python")
	commands.getoutput("sudo docker ps")
	ps=commands.getoutput("sudo docker ps | cut -d " " -f1 ")
	p1=ps.split('\n')	
	f=open("/var/www/html/users1.txt",'a')
	f.write('p1')
	f.close()
	a=commands.getoutput("sudo cat /var/www/html/users1.txt | awk '{print$1}'")	
	
	commands.getotput("sudo docker attach "a")
	ip=commands.getotput("sudo hostname -i")
	commands.getotput("sudo service shellinaboxd restart")
	commands.getotput("sudo service shellinaboxd restart")
	
	print "<html>"	
	print (" <a href='"+ip+": "+ str(port) +"' target='_blank'> Container " + str(i) +" </a>")
	print "access containers using <login - ritesh ; password - redhat >"
	print "</html>"
