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
        commands.getoutput("sudo docker run -it -p "+ str(port) +":4200  -d --name "+u+"  rahul1")

        print "<html>"
        print (" <a href='http://172.17.0.3:4200' target='_blank'> Container " + str(i) +" </a>")
        print "access containers using <login - ritesh ; password - redhat >"
        print "</html>"
