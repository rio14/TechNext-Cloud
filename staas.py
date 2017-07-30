#!/usr/bin/python2
import commands
import cgi,cgitb

print "Content-type : text/html"
print ""
cgitb.enable()
x=cgi.FieldStorage()
user=x.getvalue('usr')
password=x.getvalue('passwd')
hd=x.getvalue('hd')
#for radio button
n=x.getvalue('x')

commands.getoutput("systemctl restart httpd")
commands.getoutput("setenforce 0")
commands.getoutput("iptables -F")
#a=commands.getoutput("cat /var/www/html/users.txt | grep "+user+ " | awk '{print$1}'")
#b=commands.getoutput("cat /var/www/html/users.txt | grep "+password+ " | awk '{print$7}'")


#NFS--------------------------------------------------------------------
#if (n=="1") and (a !="") and (b !="") :
if (n=="1") :
	#1st need to create volume group(vg1)
	commands.getoutput("sudo lvcreate --name "+user+" --size "+hd+"G vg1")
	commands.getoutput("sudo mkfs.ext4 /dev/vg1/"+user+" ")
	commands.getoutput("sudo mkdir /media/"+user )
	commands.getoutput("sudo mount /dev/vg1/"+user+"  /media/"+user+"")
	commands.getoutput("sudo echo '\n /media/"+user+" *(rw,no_root_squash) \n' >>/etc/exports")
	commands.getoutput("sudo exportfs -r")
	commands.getoutput("setenforce 0")
	
	f1=open('/var/www/html/clienttar/staasclient.py','w+')
	f1.write("#!/usr/bin/python2 \nimport os \nos.system('yum install nfs-utils -y') \nos.system('systemctl restart nfs')\nos.system('setenforce 0')\nos.system('iptables -F')\nos.system('mkdir /media/mystorage')\nos.system('mount 192.168.43.103:/media/"+user+"  /media/mystorage')")  
	f1.close()
	commands.getoutput('sudo chmod 777 /var/www/html/clienttar/staasoclient.py')
	commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_staas.tar  /var/www/html/clienttar/staasclient.py")
	print  "<html>"
	print  "<p><a href='http://192.168.43.103/clienttar/"+user+"_staas.tar' download>Downlode</a>tar file and run it</p>"
	print  "</html>"

#SSHFS--------------------------------------------------------------------    
elif (n=="2") and (a !="") and (b !=""):
	#commands.getoutput("sudo useradd "+user+"")
      	#commands.getoutput("sudo echo "+passwd+"| sudo passwd "+user+" --stdin")
     	commands.getoutput("sudo lvcreate --name "+user+" --size "+hd+"G vg1")
	commands.getoutput("sudo mkfs.ext4 /dev/vg1/"+user+"")
	commands.getoutput("sudo mkdir /media/"+user+"")
	commands.getoutput("sudo mount /dev/vg1/"+user+" /media/"+user+"")
	commands.getoutput("sudo chown "+user+" /media/"+user+"")
	commands.getoutput("sudo chmod 777 /cloud/"+user+" ")

	f1=open('/var/www/html/clienttar/staasclient.py','w+')
	f1.write("\nimport commands\ncommands.getoutput('yum install fuse-sshfs')\ncommands.getoutput('systemctl restart sshfs')\ncommands.getoutput('systemctl restart sshd')\ncommands.getoutput('mkdir /root/Desktop/"+user+" ')\ncommands.getoutput('sshfs "+user+"@192.168.43.103:/"+user + " /root/Desktop/"+user+" ')\n ")
	f1.close()
	commands.getoutput('sudo chmod 777 /var/www/html/sshfs.py')
	commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_staas.tar /var/www/html/clienttar/staasclient.py")
	print  "<html>"
	print  "<p><a href='http://192.168.43.103/clienttar/"+user+"_staas.tar' download>Downlode</a> tar file and run it.......</p>"
	print  "</html>"

#ISCSI--------------------------------------------------------------------
elif (n=="3") and (a !="") and (b !=""):
	#yum install iscsi-target-utils
	commands.getoutput("sudo lvcreate --name "+user+" --size "+hd+"G vg1")
	f1=open('/etc/tgt/targets.conf','a')
	f1.write("<target "+user+">\nbacking-store /dev/vg1/"+user + "\n</target>\n")
	f1.close()
	commands.getoutput("sudo systemctl restart tgtd")

	f1=open('/var/www/html/clienttar/iscsi.py','w+')
	f1.write("\nimport commands\ncommands.getoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.98 --discover')\ncommands.getoutput('iscsiadm --mode node --targetname "+user+" --portal 192.168.43.103:3260 --login')")
	f1.close()
	commands.getoutput('sudo chmod 777 /var/www/html/clienttar/iscsi.py')
	commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_iscsi.tar /var/www/html/clienttar/iscsi.py")
	print  "<html>"
	print  "<p><a href='http://192.168.43.103/clienttar/"+user+"_iscsi.tar' download>Downlode</a> tar file and run it.......</p>"
	print  "</html>"


elif (n=="4") and (a !="") and (b !=""):
	commands.getoutput("sudo lvcreate --name "+user+" --size "+hd+"G vg1")
	commands.getoutput("sudo mkfs.ext4 /dev/vg1/"+user+"")
	commands.getoutput("sudo mkdir /media/"+user+"")
	commands.getoutput("sudo mount /dev/vg1/"+user+" /media/"+user+"")
	#commands.getoutput("sudo yum install samba samba-client")	
	commands.getoutput("sudo useradd -s /sbin/nologin "+user+"")
	commands.getoutput("sudo  echo -e '"+password+"\n"+password+"\n' |  smbpasswd -a "+user+"")
	f1=open('/etc/samba/smb.conf','a')
	f1.write("\n["+user+"]\npath = /media/"+user+"\nwritable = yes\nbrowseable = yes")
	f1.close()
	commands.getoutput("systemctl restart smb")

	f1=open('/var/www/html/clienttar/smb.py','w+')
	f1.write("\nimport commands \ncommands.getoutput('yum install cifs-utils samba-client')\ncommands.getoutput('mkdir /media/"+user+"')\ncommands.getoutput('mount -o username="+user+"//192.168.43.103/"+user+" /media/"+user+"')")
	f1.close()	
	commands.getoutput('sudo chmod 777 /var/www/html/clienttar/smb.py')
	commands.getoutput("sudo tar -cvf /var/www/html/clienttar/"+user+"_smb.tar /var/www/html/clienttar/smb.py")
	print  "<html>"
	print  "<p><a href='http://192.168.43.103/clienttar/"+user+"_smb.tar' download>Downlode</a> tar file for linux user and run it</p>"
	print "<p>Windows users go to RUN window and type IP-->//192.168.43.98 and give username and password </p>"
	print  "</html>"



	
else :
	print "<html>"
	print "Wrong user name or password"
	print "</html>"








