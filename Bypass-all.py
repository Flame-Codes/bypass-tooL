#Coding By Hannan
#Coding UTF-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass 
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Love.py')
 
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
 
def exit():
	print 'FLAME'
	os.sys.exit()
 
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
 
 
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
 
 
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mSystem in progress \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)
 
 

vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

def ban():
	jalan ("\033[1;33md8888b. db    db d8888b.  .d8b.  .d8888. .d8888. ")
	jalan ("\033[1;32m88  `8D `8b  d8' 88  `8D d8' `8b 88'  YP 88'  YP ")
	jalan ("\033[1;33m88oooY'  `8bd8'  88oodD' 88ooo88 `8bo.   `8bo.   ")
	jalan ("\033[1;32m88~~~b.    88    88~~~   88~~~88   `Y8b.   `Y8b. ")
	jalan ("\033[1;33m88   8D    88    88      88   88 db   8D db   8D ")
	jalan ("\033[1;32mY8888P'    YP    88      YP   YP `8888Y' `8888Y'")                                                                                          
	print ' '
	jalan ('\033[1;33mOWNER   : \033[1;32mFLAME-NAIM ')
	jalan ('\033[1;32mFB      : \033[1;33mNaim.Vau80')
	jalan ('\033[1;33mNOTE    : \033[1;32mTools Only For 64bit ')
	
def ok():
	os.system('clear')
	ban()
	os.system('xdg-open https://www.facebook.com/Naim.Vau80')
	jalan ('\033[1;32m[\033[1;32m1\033[1;32m] \033[1;32m-----\033[1;32m[\033[1;32mJAMES\033[1;32m]')
	jalan ('\033[1;33m[\033[1;33m2\033[1;33m] \033[1;33m-----\033[1;33m[\033[1;33mADF\033[1;33m]')
	jalan ('\033[1;32m[\033[1;32m3\033[1;32m] \033[1;32m-----\033[1;33m[\033[1;32mJUTT\033[1;32m]')
	jalan ('\033[1;33m[\033[1;33m4\033[1;33m] \033[1;33m-----\033[1;32m[\033[1;33mJUTT2\033[1;33m]')
	print (' ')
	haha = raw_input('\033[1;32m[\033[1;33m~\033[1;32m] \033[1;33mChoose: \033[1;32m')
	if haha =='':
		ok()
	elif haha =='1':
		os.system('python Prohack.py')
	elif haha =='2':
		os.system('python Adf.py')
	elif haha =='3':
		os.system('python2 number.py')
	elif haha =='4':
		os.system('python2 Juttbrand.py')
	else:
		ok()
		
ok()
		
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
