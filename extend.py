#!/usr/bin/python2
import commands
import cgi,cgitb

print "Content-type : text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
user=x.getvalue('usr')
password=x.getvalue('passwd')
nsiz=x.getvalue('ex')
n=x.getvalue('e')
commands.getoutput("systemctl restart httpd")
commands.getoutput("setenforce 0")
commands.getoutput("iptables -F")
a=commands.getoutput("cat /var/www/html/users.txt | grep "+user+ " | awk '{print$1}'")
b=commands.getoutput("cat /var/www/html/users.txt | grep "+password+ " | awk '{print$7}'")


#snap--------------------------------------------------------------------
if  (n =="1") and (a !="") and (b !="") :
	
	commands.getoutput("sudo lvextend --size +"+nsiz+" /dev/vg1/"+user)
	commands.getoutput("sudo resize2fs /dev/vg1"+user+")
	print  "<html>"
	print  "Sucsessfully Storage Extended"
	print  "</html>"

else:	
	print "<html>"
	print  "wrong user name or password ! please try again"
	print "</html>"

