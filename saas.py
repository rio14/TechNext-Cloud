#!/usr/bin/python2
import commands
import cgi,cgitb
print "Content-type : text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
user=x.getvalue('usr')
password=x.getvalue('passwd')
#for radio button
sw=x.getvalue('sw')

commands.getoutput("systemctl restart sshd")
a=commands.getoutput("cat /var/www/html/users11.txt | grep "+user+ " | awk '{print$1}'")
b=commands.getoutput("cat /var/www/html/users11.txt | grep "+password+ " | awk '{print$7}'")
	
#firefox--------------------------------------------------------------------

if ((sw=="1" )&(a!="")&(b !="")):
	f1=open('../html/clienttar/saasclient.py','w')
	f1.write("#!/usr/bin/python2 \nimport os \nos.system(\"yum install openssh-clients\") \nos.system(\"systemctl restart sshd\")\nos.system(\"ssh  -X "+user+"@192.168.43.103 firefox\") ")  
	f1.close()
	commands.getoutput('sudo chmod 777 /var/www/html/saasclient.txt')      
	commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_saas.tar /var/www/html/clienttar/saasclient.py")
	print  "<html>"
	print  "<a href='http://192.168.43.103/clienttar/"+user+"_saas.tar' download>Submit this</a>"
	print  "</html>"

#gedit--------------------------------------------------------------------
elif (sw=="2" ) and (a !="") and (b !=""):
	f1=open('/var/www/html/clienttar/saasclient.py','w+')
	f1.write("#!/usr/bin/python2 \nimport os \nos.system(\"yum install openssh-clients\") \nos.system(\"systemctl restart sshd\")\nos.system(\"ssh  -X "+user+"@192.168.43.103 gedit\") ")  
	f1.close()
	commands.getoutput('sudo chmod 777 /var/www/html/saasclient.txt')      
	commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_saas.tar /var/www/html/clienttar/saasclient.py")

	print  "<html>"
	print  "<a href='http://192.168.43.103/clienttar/"+user+"_saas.tar' download>submit</a>"
	print  "</html>"



else :
 	print  "<html>"
	
	print	"wrong username or password go back and login again"
	print  "</html>" 

	
