from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gspread_util import *
from parse_util import *
import time
import pprint

pp = pprint.PrettyPrinter()
chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}

chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com")
wait = WebDriverWait(driver, 100)


def login():
	username = 'nicrobert4747@gmail.com'
	password ='connversation123'
	driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
	driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
	driver.find_element_by_xpath('//*[@value="Log In"]').click()

def find_group_info(group_list):
	item = 0	
	for group in group_list:
		if item < 87:
			item += 1
			continue
		if group == 'Text':
			continue
		# if group not 'https://www.facebook.com/ProudBoysSyd/?ref=br_rs':
		# 	continue
		print(f"fetching {group}")
		driver.get(group)
		time.sleep(2)
		raw_name = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/span/div/span[1]/span/h1/a/span') #') and contains(.//span, "people like this")]')votelocal - great lakes
		name = raw_name.text
		h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._4-u2._6590._3xaf._4-u8'))) #
		try:
			likes = driver.find_element_by_xpath('//div[contains(@class, "_4bl9") and contains(.//div, "people like this")]')
			tlikes = likes.text
		except:
			likes = driver.find_element_by_xpath('//div[contains(@class, "_4bl9") and contains(.//div, "person likes this")]')
			tlikes = likes.text


		info_ads = driver.find_element_by_xpath('//div[@data-key ="tab_ads"]')
		info_ads.click()

		h3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._4-u2._15x_._3-96._4-u8'))) #
			#, '//*[@id="u_fetchstream_1_1"]/div[1]/div[1]/div/div')))
		try:
			created = driver.find_element_by_xpath('//span[contains(@class, "_2ien")]')
			date = created.text
		except:
			date = 'what??'

		try:
			#created = driver.find_element_by_css_selector("#u_fetchstream_1_0 > div._4-u2._15x_._3-96._4-u8 > div:nth-child(2) > span") #]
			names = driver.find_elements_by_xpath('//span[contains(@class, "_2ien") and contains(.//div, "Previously named")]')
			if len(names) > 1:
				previous_names = parse_names(names)
			else:
				previous_names = names.text
		except:
			previous_names = 'No name change'
		# previous_names = 'to implement'
		# try:
		# 	old_names = driver.find_element_by_css_selector('#u_fetchstream_1_0 > div._4-u2._15x_._3-96._4-u8 > div:nth-child(3) > div:nth-child(2) > span > div > span')
		# 	previous_names = old_names.text
		# except:
		# 	previous_names = 'Null' 
		save_Pageinfo(group, tlikes, date, previous_names, name)
#u_fetchstream_1_1 > div._4-u2._15x_._3-96._4-u8 > div:nth-child(2) > span
#u_fetchstream_2_1 > div._4-u2._15x_._3-96._4-u8 > div:nth-child(2) > span

#u_0_15 > div._4-u2._15x_._3-96._4-u8 > div:nth-child(3) > span
def search_facebook():
	search_query = 'https://www.facebook.com/search/str/votelocal/keywords_groups'
	driver.get(search_query)
	item = 1	
	while item < 10:
		item += 1
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(3)
		print(item)

	links = driver.find_elements_by_class_name('_32mo')
	urls = []
	for link in links:
		url = link.get_attribute('href')
		urls.append(url)
		print(url)
	return urls




def main():
	group_list = find_groups()
	print(group_list) 
	login()
	search(group_list)


if __name__ == '__main__':
	login()
	urls = search_facebook()
	write_groups(urls)
	urls = find_groups()
	find_group_info(urls)

