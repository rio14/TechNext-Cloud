#!/usr/bin/python2
import os,cgitb
import commands
import cgi
print "Content-type: text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
u=x.getvalue('usr')
e=x.getvalue('email')
m=x.getvalue('mob')
p=x.getvalue('passwd')
p1=x.getvalue('passwd1')
a=commands.getoutput("sudo cat /var/www/html/users.txt | grep "+u+" | awk '{print$1}'")
if (a != ""):	
	print "this user already exist"	
else :
	f=open("/var/www/html/users.txt",'a')
	f.write(u)
	f.write(" : ")
	f.write(e)
	f.write(" : ")
	f.write(m)
	f.write(" : ")
	f.write(p)
	f.write(" : ")
	f.write(p1)
	f.write(" : ")
	f.write("\n")
	f.close()
	os.system("sudo useradd  "+u+"")
 	os.system("sudo echo "+p1+"|sudo passwd "+u+" --stdin ")
	print "location:http://192.168.43.103/.html"
		
		






