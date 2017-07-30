#!/usr/bin/python2
import os,cgitb
import commands
import cgi
print "Content-type: text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
u=x.getvalue('usr')
p=x.getvalue('passwd')

a=commands.getoutput("cat /var/www/html/users11.txt |grep "+u+ " | awk '{print$1}'")
b=commands.getoutput("cat /var/www/html/users11.txt |grep "+p+ " | awk '{print$5}'")

if (a != "") and (b !=""):
		
		print "<a href='http://192.168.43.103/home.html'>click here</a>"
		print " "
	
else:
	print "wrong user name or password try again"
	print " "
	
	
