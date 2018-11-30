import requests
import re
from time import sleep

def find_ip(html):
	regex = r"(IP address: )(.*?)(?=<br>)"
	matches = re.search(regex, html, re.MULTILINE)
	# print(matches[2])
	return matches.group(2)

username = "niccdias"
password = "bM65lMa99ybZcd0r"

PROXY_RACK_DNS = "megaproxy.rotating.proxyrack.net:222"

test1 = "http://ip-api.com/json"
test2 = "http://httpbin.org/ip"
test3 = "https://api.ipify.org?format=json"

proxy = {"http":"http://{}:{}@{}".format(username, password, PROXY_RACK_DNS)}
url = 'https://www.google.com/search?q=site%3Aafp.com+comprova+%28investigado+OR+projeto+OR+%22fake+news%22+OR+%22not%C3%ADcias+falsas%22+OR+boatos+OR+verificado+OR+fact-check+OR+factcheck%29&amp;num=100&amp;start=0'
r = requests.get(url , proxies=proxy)
ip = find_ip(r.text)	
if ip is not None:
	print(f"google thinks ip is : {ip}")
if ip == None:
	print(r.text)
sleep(15)
# print(response.text)
r1 = requests.get(url , proxies=proxy)
ip1 = find_ip(r.text)
if ip1 is not None:
	print(f"google thinks ip is : {ip1}")
if ip1 == None:
	print(r.text)
r2= requests.get(url , proxies=proxy)
ip2 = find_ip(r.text)
if ip2 is not None:
	print(f"google thinks ip is : {ip2}")
if ip2 == None:
	print(r.text)
r3 = requests.get(test3 , proxies=proxy)
print(f"test 3: {r3.text}")
r4 = requests.get(test1 , proxies=proxy)
print(f"test 4: {r4.text}")
r5= requests.get(test2 , proxies=proxy)
print(f"test 5: {r5.text}")
r6 = requests.get(test3, proxies=proxy)
print(f"test 6: {r6.text}")


# print("Response:\n{}".format(r.text))	

