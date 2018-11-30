from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pprint
import pandas as pd
import ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}

chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)

def main():
	# wait = WebDriverWait(driver, 100)
	queries = [#'site:checamos.afp.com comprova',
		# 'site:band.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		# 'site:bandnewstv.band.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:correiodopovo.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:exame.abril.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:folha.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:gauchazh.clicrbs.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:gazetadopovo.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:gazetaonline.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:jconline.ne10.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:metrojornal.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:nexojornal.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:nsccomunicacao.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:estadao.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:opovo.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:poder360.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:bandnewsfm.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:radiobandeirantes.band.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:novaescola.org.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:piaui.folha.uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:sbt.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:futura.org.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:uol.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)',
		'site:veja.abril.com.br comprova (investigado OR projeto OR "fake news" OR "notícias falsas" OR boatos OR verificado OR fact-check OR factcheck)']

	result_list = []
	item = 0 
	try:
		for query in queries:
			if item >= 3:
				time.sleep(130)
			driver.get("https://www.google.com/")
			search = driver.find_element_by_css_selector('.gLFyf.gsfi')
			search.send_keys(query)
			search.send_keys(Keys.RETURN)
			time.sleep(3)
			while "www.google.com/sorry/index?" in driver.current_url:
				Mbox('Captcha identified', 'Solve Captcha Please', 0)
				print('sslee[ong')
				time.sleep(36)
			# captcha = driver.find_element_by_css_selector('#recaptcha-anchor-label')
			# print(captcha)
			# if captcha:
			# 	print('sleeping')
			# 	time.sleep(35)
			# except:
			# 	pass
			try:
				next_page = driver.find_element_by_css_selector('#pnnext')
			except: 
				next_page = 'once'
			while next_page:
				try:
					captcha = driver.find_element_by_css_selector('#recaptcha-anchor-label')
					if captcha:
						Mbox('Captcha identified', 'Solve Captcha Please', 0)
						print('sleeping')
						time.sleep(35)
				except:
					pass
				links = driver.find_elements_by_class_name('r')
				for link in links:
					actual_link = link.find_element_by_css_selector('a')
					true_link = actual_link.get_attribute('href')
					title = link.find_element_by_class_name('LC20lb').text

					result_dict = {'link': true_link,
							'title': title}

					result_list.append(result_dict)

					print(f"{actual_link} and {title}")
				if next_page == 'once':
					break
				driver.execute_script("arguments[0].scrollIntoView();", next_page)
				next_page.click()
				try:
					next_page = driver.find_element_by_css_selector('#pnnext')
				except:
					break
	except Exception as e:
		print(e)

	df = pd.DataFrame(result_list)
	df.to_csv('comprovaArticleScrape.csv', index = False)





if __name__ == '__main__':
	main()