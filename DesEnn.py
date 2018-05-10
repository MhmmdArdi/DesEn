import hashlib
import os
import time
import urllib
import urllib2
import re

B = '\033[1;36m'
R = '\033[1;31m'
W = '\033[1;0m'
H = '\033[1;33m'
K = '\033[1;34m'

os.system("clear")

index = """\033[1;31m
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
	print("""\033[1;36m
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
			b = raw_input("\033[1;34m[Md5 Encrpyt]>>")
			md5 = hashlib.md5(b.encode())
			print "Code You>>>",md5.hexdigest()
			print ""
			main()
			
			
		elif x == "2":
			os.system("clear")
			print(index)
			string=raw_input("\033[1;33mpaste MD5 Hash > ")
			website = 'http://md5decryption.com/'
			weburl = urllib.urlencode({'hash':string,'submit':'Decrypt+It!'})
			req = urllib2.Request(website)
			try:
				  fd = urllib2.urlopen(req, weburl)
				  data = fd.read()
				  match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
				  if match: print '[-] site: %s\t\t\tPassword: %s' % (website, match.group(2))
				  else: print '[-] site: %s\t\t\tPassword: Not found' % website
			except urllib2.URLError: print '[+] site: %s \t\t\t[+] Error: seems to be down' % website
			main()
		else:
			print ""
			print "\033[1;32mCommand >> --Menu Bro"
			print ""
			print "\033[1;33mNo Command >>",x
			print ""
			main()
if __name__ == "__main__":
	main()