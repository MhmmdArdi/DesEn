import hashlib
import os
import time
import urllib
import urllib2
import re
os.system("clear")

index = """
    __     __          _                  _____                   
    \ \   / /         | |                / ____|                  
     \ \_/ /   _ _ __ | | _____ _ __ ___| |     _ __ _____      __
      \   / | | | '_ \| |/ / _ \ '__/ __| |    | '__/ _ \ \ /\ / /
       | || |_| | | | |   <  __/ |  \__ \ |____| | |  __/\ V  V / 
       |_| \__,_|_| |_|_|\_\___|_|  |___/\_____|_|  \___| \_/\_/  
    https://github.com/MhmmdArdi                        Mr.Ardi
*******************************************************************
[#] EncrpytMd5 Or Descrypt Md5 (#)
"""

print(index)


def Menu():
	os.system("clear")
	print(index)
	print("""
	 1  Md5 Encrypt
	 2  Md5 Descrypt
""")

def main():
		x = raw_input("[?]>>>")
		if x == "--Menu":
			time.sleep(2)
			Menu()
			main()
		
	
		elif x == "1":
			os.system("clear")
			print(index)
			b = raw_input("[Md5 Encrpyt]>>")
			md5 = hashlib.md5(b.encode())
			print "Code You>>>",md5.hexdigest()
			print ""
			main()
			
			
		elif x == "2":
			os.system("clear")
			string=raw_input("paste MD5 Hash > ")
			website = 'https://hashkiller.co.uk/'
			weburl = urllib.urlencode({'hash':string,'submit':'Decrypt+It!'})
			req = urllib2.Request(website)
			try:
				  fd = urllib2.urlopen(req, weburl)
				  data = fd.read()
				  match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
				  if match: print '[-] site: %s\t\t\tPassword: %s' % (website, match.group(2))
				  else: print '[-] site: %s\t\t\tPassword: Not found' % website
			except urllib2.URLError: print '[+] site: %s \t\t\t[+] Error: seems to be down' % website
			
		else:
			print ""
			print "Command >> --Menu Bro"
			print ""
			print "No Command >>",x
			print ""
			main()
if __name__ == "__main__":
	main()