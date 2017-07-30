#!/usr/bin/python

import cgi

print "Content-type:text/html"
x=cgi.FieldStorage()
q=x.getvalue('q')
print ""

if(q=='sucess'):
	print "<script>alert('os sucessfuly created');</script>"
	print "location:http://192.168.43.98/cgi-bin/ias.py"
print """
<head><center><h1>IAAS</h1></center></head>
<body>
	<form method="post" action="http://192.168.43.98/cgi-bin/iaas.py">
                <h2>Selecttt Your operating System</h2>
		<h3>LINUX :<input type="radio"  value="1" name="y" /></h3>
                <h3>Windows :<input type="radio" value="2" name="y"/></h3>
	
 		<br>Enter os name  : <input type='text' name='name' /></br>
		<br>Enter core cpu's  : <input type='text' name='cpu' /></br>
		<br>Enter RAM size : <input type='text' name='ram' /></br>
		
		<h2>Select installation method</h2>
		
		Live boot<input type="radio" value="1" name="radio" />
		Manually Install<input type="radio"  value="2" name="radio" />
               
        	 
		<input type='submit' value="lounch instance" /></form>
	<form>Select core cpu's:
			<select id="cpu" onchange="preferedBrowser()">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="2">3</option>
			</select>
		</form>

</body>
</html>"""
