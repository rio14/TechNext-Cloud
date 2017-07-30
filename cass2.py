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
	ip=commands.getstatusoutput("sudo docker run -itd -p "+ str(port)+":4200  rahul14 ")
	#commands.getoutput("sudo docker attach "+u+" ")
	commands.getoutput("sudo docker exec -t "+ip[1]+"  service shellinaboxd restart")
	#commands.getoutput("sudo  service shellinaboxd restart")
	#ip=commands.getoutput("sudo hostname -i")
	print "<html>"	
	print " <a href='http://192.168.43.103:"+ str(port)+"' target='_blank'> Container " + str(i) +" </a>"
	print "access containers using login - ritesh ; password - redhat "
	print "</html>"
