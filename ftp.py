import requests
import requests_ftp
import bs4
import re
import random

p_list = []
data = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

# POPULATE PROXIES
def pp():
	kk = requests.get('https://free-proxy-list.net/')
	soup = bs4.BeautifulSoup(kk.text,'lxml')
	kkk = soup.find('tbody')
	rows = kkk.find_all('tr')
	for row in rows:
	    cols = row.find_all('td')
	    cols = [ele.text.strip() for ele in cols]
	    data.append([ele for ele in cols if ele])
	for i in data:
		if i[6]=='yes':
			p_list.append("https://"+i[0]+":"+i[1])

#FTP ATTACK
def ftp():
	proxies = {'https': p_list[random.randint(0,len(p_list)-1)]}
	print(proxies)
	requests_ftp.monkeypatch_session()
	with requests.Session() as s:
		s.proxies.update(proxies)
		# r = s.get(r'http://jsonip.com', headers=headers)
		# ip= r.json()['ip']
		# print('Your IP is', ip)
		resp = s.list('ftp://90.130.70.73/', auth=('anonymous', 'anonymous'))
		print(resp)

pp()
for i in range(100):
	ftp()