#!/usr/bin/python2

import cgitb,cgi,commands,random

print "Contant-type:text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
p1=x.getvalue("cho")
u=x.getvalue('uname')
p=x.getvalue('pas')

port=random.randint(6000,7000)
commands.getoutput("sudo systemctl restart docker")

if p1=="1" :
	ip=commands.getstatusoutput("sudo docker run -itd -p "+ str(port)+":4200  pythom12 ")
	commands.getoutput("sudo docker exec -t "+ip[1]+"  service shellinaboxd restart")
	print "<html>"	
	print "<a href='http://192.168.43.103:"+ str(port)+"' target='_blank'> python platform </a>"
	print "access containers using login - rio ; password - 14 "
	print "</html>"
elif p1=="1" :
	ip=commands.getstatusoutput("sudo docker run -itd -p "+ str(port)+":4200  pythom12 ")
	commands.getoutput("sudo docker exec -t "+ip[1]+"  service shellinaboxd restart")
	print "<html>"	
	print " <a href='http://192.168.43.103:"+ str(port)+"' target='_blank'> bash platform </a>"
	print "access containers using login - ritesh14 ; password - redhat "
	print "</html>"
