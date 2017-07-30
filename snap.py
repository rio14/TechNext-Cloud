#!/usr/bin/python2
import commands
import cgi,cgitb

print "Content-type : text/html"
print 
cgitb.enable()
x=cgi.FieldStorage()
user=x.getvalue('usr')
password=x.getvalue('passwd')

commands.getoutput("systemctl restart httpd")
commands.getoutput("setenforce 0")
commands.getoutput("iptables -F")
a=commands.getoutput("cat /var/www/html/users.txt | grep "+user+ " | awk '{print$1}'")
b=commands.getoutput("cat /var/www/html/users.txt | grep "+password+ " | awk '{print$7}'")


#snap--------------------------------------------------------------------
if  (a !="") and (b !="") :
	
	commands.getoutput("sudo lvcreate --name snap_"+user+" --size 100M -s /dev/vg1/"+user)
	commands.getoutput("sudo mkdir /var/www/clientsnap/snap_"+user)
	commands.getoutput("sudo mount /dev/vg1/"+user+" /var/www/clientsnap/snap_"+user)
	
	commands.getoutput("sudo echo '\n /var/www/directory/"+user+" *(rw,no_root_squash) \n' >>/etc/exports")
	commands.getoutput("sudo exportfs -r")
	commands.getoutput("setenforce 0")
	
	f1=open('/var/www/html/clienttar/snap.py','w+')
	f1.write("#!/usr/bin/python2 \nimport os \nos.system('yum install nfs-utils -y') \nos.system('systemctl restart nfs')\nos.system('setenforce 0')\nos.system('iptables -F')\nos.system('mkdir /root/Desktop/mysnap')\nos.system('mount 192.168.43.98:/var/www/clientsnap/snap_"+user+"  /root/Desktop/mysnap')")  
	f1.close()
	commands.getoutput('sudo chmod 777 /var/www/html/clienttar/snap.py')
	commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_snap.tar  /var/www/html/clienttar/snap.py")
	print  "<html>"
	print  "<a href='http://192.168.43.98/clienttar/"+user+"_snap.tar' download>submit</a>"
	print  "</html>"

else:	print "<html>"
	print  "wrong user name or password ! please try again"
	print "</html>"

