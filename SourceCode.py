print'EasyProxy'
print'Developed by 'Undercore'
print'version 1.0'
print'[%]scraping started'
import urllib
import re
from time import gmtime, strftime, sleep

def writetofile(lines):
	for line in lines:
		wfile.write(line + "\n")

def process	(source):
	proxys = []
	templist = []
	temp = ""
	
	for line in source:
		temp += line
		
	z = 0
	prt1 = ""
	prt2 = ""
	for itm in temp:
		if ":" in itm:
			prt1 = temp[z - 15:z]
			prt2 = temp[z:z + 6]
			templist.append(prt1 + prt2)
		z += 1
			
	for line in templist:
		if re.compile('a-z').match(line) is not None:
			proxys.append(line)
			
	x = 0
	for line in proxys:
		temp = ""
		for itm in line:
			if re.compile('[0-9.:]').match(itm) is not None:
				temp += itm
				proxys[x] = temp
		x += 1
	return proxys
	
		
#The Websites proxies are gonna be scraped from, currently, unknown	
urls = ["http://50kproxies.com/10-february-10-02-new-fresh-daily-50000-proxy-list-50kproxies-com/",
"http://50kproxies.com/11-january-11-01-new-fresh-daily-50000-proxy-list-50kproxies-com/",
"http://50na50.net/",
"http://50na50.net/proxy/httplist",
"http://50na50.net/no_anonim_http.txt",
"http://aliveproxy.com/anonymous-proxy-list",
"http://aliveproxy.com/ca-proxy-list",
"http://aliveproxy.com/fastest-proxies",
"http://aliveproxy.com/fr-proxy-list",
"http://aliveproxy.com/gb-proxy-list",
"http://aliveproxy.com/high-anonymity-proxy-list",
"http://aliveproxy.com/jp-proxy-list",
"http://aliveproxy.com/proxy-list-port-3128",
"http://aliveproxy.com/proxy-list-port-80",
"http://aliveproxy.com/proxy-list-port-8000",
"http://aliveproxy.com/proxy-list-port-8080",
"http://aliveproxy.com/ru-proxy-list",
"http://aliveproxy.com/us-proxy-list",
"http://atomintersoft.com/anonymous_proxy_list",
"http://atomintersoft.com/high_anonymity_elite_proxy_list",
"http://atomintersoft.com/products/alive-proxy/proxy-list",
"http://atomintersoft.com/products/alive-proxy/proxy-list?ap=9",
"http://atomintersoft.com/products/alive-proxy/proxy-list/3128",
"http://atomintersoft.com/products/alive-proxy/proxy-list/com",
"http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/",
"http://atomintersoft.com/products/alive-proxy/socks5-list",
"http://atomintersoft.com/proxy_list_domain_com",
"http://atomintersoft.com/proxy_list_domain_edu",
"http://atomintersoft.com/proxy_list_domain_net",
"http://atomintersoft.com/proxy_list_domain_org",
"http://atomintersoft.com/proxy_list_port_3128",
"http://atomintersoft.com/proxy_list_port_80",
"http://atomintersoft.com/proxy_list_port_8000",
"http://atomintersoft.com/proxy_list_port_81",
"http://atomintersoft.com/transparent_proxy_list",
"http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any",
"http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any&p=2",
"http://best-proxy.com/english/search.php?search=anonymous-and-elite&country=any&type=anonymous-and-elite&port=any&ssl=any&p=3",
"http://bestproxy.narod.ru/proxy2.html",
"http://checkerproxy.net/all_proxy",
"http://ejohn.org/apps/anon/",
"http://free-proxy-list.net/",
"http://free-proxy-list.net/anonymous-proxy.html",
"http://free-proxy-list.net/uk-proxy.html",
"http://guncelproxy.com/Anasayfa/",
"http://multiproxy.org/anon_proxy.htm",
"http://multiproxy.org/txt_all/proxy.txt",
"http://nntime.com/proxy-list-01.htm",
"http://nntime.com/proxy-list-02.htm",
"http://nntime.com/proxy-list-03.htm",
"http://nntime.com/proxy-list-04.htm",
"http://nntime.com/proxy-list-05.htm",
"http://nntime.com/proxy-list-06.htm",
"http://nntime.com/proxy-list-07.htm",
"http://nntime.com/proxy-list-08.htm",
"http://nntime.com/proxy-list-09.htm",
"http://nntime.com/proxy-list-10.htm",
"http://nntime.com/proxy-list-11.htm",
"http://nntime.com/proxy-list-12.htm",
"http://nntime.com/proxy-list-13.htm",
"http://nntime.com/proxy-list-14.htm",
"http://nntime.com/proxy-list-15.htm",
"http://nntime.com/proxy-list-17.htm",
"http://nntime.com/proxy-list-18.htm",
"http://nntime.com/proxy-list-19.htm",
"http://nntime.com/proxy-list-20.htm",
"http://nntime.com/proxy-list-21.htm",
"http://nntime.com/proxy-list-22.htm",
"http://nntime.com/proxy-list-23.htm",
"http://nntime.com/proxy-list-24.htm",
"http://nntime.com/proxy-list-25.htm",
"http://nntime.com/proxy-list-27.htm",
"http://nntime.com/proxy-list-28.htm",
"http://nntime.com/proxy-list-29.htm",
"http://nntime.com/proxy-list-30.htm",
"http://notan.h1.ru/hack/xwww/proxy1.html",
"http://notan.h1.ru/hack/xwww/proxy10.html",
"http://notan.h1.ru/hack/xwww/proxy2.html",
"http://notan.h1.ru/hack/xwww/proxy3.html",
"http://notan.h1.ru/hack/xwww/proxy4.html",
"http://notan.h1.ru/hack/xwww/proxy5.html",
"http://notan.h1.ru/hack/xwww/proxy6.html",
"http://notan.h1.ru/hack/xwww/proxy7.html",
"http://notan.h1.ru/hack/xwww/proxy8.html",
"http://notan.h1.ru/hack/xwww/proxy9.html",
"http://proxy.speedtest.at/proxybyActuality.php?offset=0",
"http://proxy.speedtest.at/proxybyActuality.php?offset=100",
"http://proxy.speedtest.at/proxybyActuality.php?offset=125",
"http://proxy.speedtest.at/proxybyActuality.php?offset=150",
"http://proxy.speedtest.at/proxybyActuality.php?offset=175",
"http://proxy.speedtest.at/proxybyActuality.php?offset=200",
"http://proxy.speedtest.at/proxybyActuality.php?offset=225",
"http://proxy.speedtest.at/proxybyActuality.php?offset=25",
"http://proxy.speedtest.at/proxybyActuality.php?offset=250",
"http://proxy.speedtest.at/proxybyActuality.php?offset=275",
"http://proxy.speedtest.at/proxybyActuality.php?offset=300",
"http://proxy.speedtest.at/proxybyActuality.php?offset=325",
"http://proxy.speedtest.at/proxybyActuality.php?offset=350",
"http://proxy.speedtest.at/proxybyActuality.php?offset=375",
"http://proxy.speedtest.at/proxybyActuality.php?offset=400",
"http://proxy.speedtest.at/proxybyActuality.php?offset=425",
"http://proxy.speedtest.at/proxybyActuality.php?offset=450",
"http://proxy.speedtest.at/proxybyActuality.php?offset=475",
"http://proxy.speedtest.at/proxybyActuality.php?offset=50",
"http://proxy.speedtest.at/proxybyActuality.php?offset=500",
"http://proxy.speedtest.at/proxybyActuality.php?offset=525",
"http://proxy.speedtest.at/proxybyActuality.php?offset=550",
"http://proxy.speedtest.at/proxybyActuality.php?offset=575",
"http://proxy.speedtest.at/proxybyActuality.php?offset=600",
"http://proxy.speedtest.at/proxybyActuality.php?offset=625",
"http://proxy.speedtest.at/proxybyActuality.php?offset=650",
"http://proxy.speedtest.at/proxybyActuality.php?offset=675",
"http://proxy.speedtest.at/proxybyActuality.php?offset=700",
"http://proxy.speedtest.at/proxybyActuality.php?offset=75",
"http://proxylist.sakura.ne.jp/index.htm?pages=0",
"http://proxylist.sakura.ne.jp/index.htm?pages=1",
"http://proxylist.sakura.ne.jp/index.htm?pages=2",
"http://proxylist.sakura.ne.jp/index.htm?pages=3",
"http://proxylist.sakura.ne.jp/index.htm?pages=4",
"http://proxylistchecker.org/proxylists.php",
"http://proxylistchecker.org/proxylists.php?t=&p=10",
"http://proxylistchecker.org/proxylists.php?t=&p=2",
"http://proxylistchecker.org/proxylists.php?t=&p=3",
"http://proxylistchecker.org/proxylists.php?t=&p=4",
"http://proxylistchecker.org/proxylists.php?t=&p=5",
"http://proxylistchecker.org/proxylists.php?t=&p=6",
"http://proxylistchecker.org/proxylists.php?t=&p=7",
"http://proxylistchecker.org/proxylists.php?t=&p=8",
"http://proxylistchecker.org/proxylists.php?t=&p=9",
"http://rootjazz.com/proxies/proxies.txt",
"http://samair.ru/proxy/proxy-01.htm",
"http://samair.ru/proxy/proxy-02.htm",
"http://samair.ru/proxy/proxy-03.htm",
"http://samair.ru/proxy/proxy-04.htm",
"http://samair.ru/proxy/proxy-05.htm",
"http://samair.ru/proxy/proxy-06.htm",
"http://samair.ru/proxy/proxy-07.htm",
"http://samair.ru/proxy/proxy-08.htm",
"http://samair.ru/proxy/proxy-09.htm",
"http://samair.ru/proxy/proxy-10.htm",
"http://samair.ru/proxy/proxy-11.htm",
"http://samair.ru/proxy/proxy-12.htm",
"http://samair.ru/proxy/proxy-13.htm",
"http://samair.ru/proxy/proxy-14.htm",
"http://samair.ru/proxy/proxy-15.htm",
"http://samair.ru/proxy/proxy-16.htm",
"http://samair.ru/proxy/proxy-17.htm",
"http://samair.ru/proxy/proxy-18.htm",
"http://samair.ru/proxy/proxy-19.htm",
"http://samair.ru/proxy/proxy-20.htm",
"http://samair.ru/proxy/proxy-21.htm",
"http://samair.ru/proxy/proxy-22.htm",
"http://samair.ru/proxy/proxy-23.htm",
"http://samair.ru/proxy/proxy-24.htm",
"http://samair.ru/proxy/proxy-25.htm",
"http://samair.ru/proxy/proxy-26.htm",
"http://samair.ru/proxy/proxy-27.htm",
"http://samair.ru/proxy/proxy-28.htm",
"http://samair.ru/proxy/proxy-29.htm",
"http://samair.ru/proxy/proxy-30.htm",
"http://spys.ru/en/anonymous-proxy-list/",
"http://spys.ru/en/free-proxy-list/",
"http://tools.rosinstrument.com/proxy/?rule1",
"http://txt.proxyspy.net/proxy.txt",
"http://vmarte.com/proxy/proxy_all.txt",
"http://www.getproxy.jp/en/default/1",
"http://www.getproxy.jp/en/default/2",
"http://www.getproxy.jp/en/default/3",
"http://www.getproxy.jp/en/default/4",
"http://www.getproxy.jp/en/default/5",
"http://www.google-proxy.net/",
"http://www.ip-adress.com/proxy_list/?k=time&d=desc",
"http://www.my-proxy.com/free-proxy-list.html",
"http://www.proxy4ever.com/",
"http://www.proxyblind.org/anonymous-proxy.shtml",
"http://www.proxyblind.org/free-proxy.shtml",
"http://www.proxyblind.org/proxy-list.shtml",
"http://www.proxyblind.org/ssl.shtml",
"http://www.proxyforest.com/proxy.htm",
"http://www.socks-proxy.net/",
"http://www.ultrasurf.org/",
"http://www.us-proxy.org/",]
		
for c in range(2, 11):
	urls.append("http://proxy-list.org/english/index.php?p=" + str(c))
for c in range(2,31):
	if c < 10:
		urls.append("http://www.samair.ru/proxy/proxy-0" + str(c) + ".htm")
	else:
		urls.append("http://www.samair.ru/proxy/proxy-" + str(c) + ".htm")
		

timestamp = strftime("%d, %b, %Y, %H, %M, %S", gmtime())
wfile = open("proxies" + timestamp + ".txt","w")

proxycount = 0
for x in range(len(urls)):
	proxies = []
	try:
		response = urllib.urlopen(urls[x])
	except Exception as e:
		print "An error occured at {}".format(urls[x])
		continue
	print "[%]Grabbing " + urls[x]
	html = response.read()
	response.close()
	proxies += process(html)
	writetofile(proxies)
	proxycount += len(proxies)
	sleep(1)

	
print "Grabbing proxies finished, proxies scraped and saved!: " + str(proxycount)	
wfile.close()
