import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from random import choice
from os import system
from stem import Signal		
from stem.control import Controller
import re

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return results


def get_tor_session():
	global session
	session = requests.session()

	session.proxies = {'http':  'socks5://127.0.0.1:9050',
					   'https': 'socks5://127.0.0.1:9050'}

def renew_connection():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)

keywords = ['site:afp.com comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:band.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)'] #'site:bandnewstv.band.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:correiodopovo.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:exame.abril.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:folha.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:gauchazh.clicrbs.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:gazetadopovo.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:gazetaonline.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:jconline.ne10.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:metrojornal.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:nexojornal.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:nsccomunicacao.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:estadao.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:opovo.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:poder360.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:bandnewsfm.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:radiobandeirantes.band.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:novaescola.org.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:piaui.folha.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:sbt.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:futura.org.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)','site:veja.abril.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)']


def fetch_results(search_term, number_results, start):
	assert isinstance(search_term, str), 'Search term must be a string'
	assert isinstance(number_results, int), 'Number of results must be an integer'
	escaped_search_term = search_term.replace(' ', '+').replace(':', '%3A').replace('(', '%28').replace('"', '%22').replace(')', '%29')
	username = "niccdias"
	password = "bM65lMa99ybZcd0r"
	PROXY_RACK_DNS = "megaproxy.rotating.proxyrack.net:222"

	
	google_url = f'https://www.google.com/search?q={escaped_search_term}&num={number_results}&start={start}'
	proxy = {"http":"http://{}:{}@{}".format(username, password, PROXY_RACK_DNS)}
	print('Proxy Below')
	print(proxy)
	print('URL Below')
	print(google_url)
	user_agents = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
	'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
	'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11',
	'Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2']
	
	s = requests.session()
	USER_AGENT = {'User-Agent': choice(user_agents)}
	response = s.get(google_url)  # proxies=proxy, headers = USER_AGENT)
	s.cookies.clear()
	print(response.text)

	# response = session.get(google_url, headers=USER_AGENT)
	# response.raise_for_status()

	return search_term, response.text, start


def parse_results(html, keyword, start):
	soup = BeautifulSoup(html, 'html.parser')

	found_results = []
	rank = 1 + start
	result_block = soup.find_all('div', attrs={'class': 'g'})
	for result in result_block:
		link = result.find('a', href=True)
		title = result.find('h3')
		description = result.find('span', attrs={'class': 'st'})
		if link and title:
			link = link['href']
			title = title.get_text()
			if description:
				description = description.get_text()
			if link != '#':
				found_results.append({'keyword': keyword, 'rank': rank, 'title': title, 'description': description, 'link': link})
				rank += 1
	return found_results

def find_ip(html):
	regex = r"(IP address: )(.*?)(?=<br>)"
	matches = re.search(regex, html, re.MULTILINE)
	# print(matches[2])
	return matches.group(2)

	
def scrape_google(search_term, number_results):
	start = 0
	fail_count = 0
	finalResults = {}
	done = False
	while not done and fail_count < 15:   
		try:
			keyword, html, start = fetch_results(search_term, number_results, start)
			results = parse_results(html, keyword, start)
			# print(html)
			print('')
			print('!!!!!!!!!!!!!!!!!!!!!!')
			ip = find_ip(html)
			print(ip)
			if "CAPTCHA" in html: #tries again with same query
				fail_count += 1
				print(f'Got rate Limited for the {fail_count} time, we GO AGANE')
				print('')
				continue

			if "pnnext" not in html:  #sensitive, should implement better check but works
				done = True
				print('!!!!!!!!!!!!')
				print('Done Scraping')
				print('!!!!!!!!!!!!')
				continue

				
			print('!!!!!!!!!!!!!!!!!!!')
			print('SUCCESS')
			print('!!!!!!!!!!!!!!!!!!!')
			print(results)
			start += 100
		except Exception as e:
			# keyword, html, start = fetch_results(search_term, number_results, start)
			print('We Go Again but Why?')
			
			# start += 100
			print(e)
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
			# break
		try:
			finalResults= merge_dicts(results)
			# finalResults.append(results)
		except:
			pass
		# except AssertionError:
		#	 raise Exception("Incorrect arguments parsed to function")
		# except requests.HTTPError:
		#	 print("You appear to have been blocked by Google. Re-routing through Tor.")
			# renew_connection()
		#	 get_tor_session()
		
		# except requests.Reques	Appears to be an issue with your connection")

	return finalResults, True

if __name__ == '__main__':
	data = []

	# get_tor_session()

	for keyword in keywords:
		try:
			results, abort = scrape_google(keyword, 100)
			for result in results:
				data.append(result)
			if abort:
				break

		except Exception as e2:
			print(e2)
		finally:
			# sleep(10)
			pass
	
	df = pd.DataFrame(data)
	df.to_csv('comprova_googleResults.csv', index=False)