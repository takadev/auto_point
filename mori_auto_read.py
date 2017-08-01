import sys
import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

inifile = ConfigParser.SafeConfigParser()
inifile.read('./config.ini')
mail = inifile.get('settings', 'id')
passwd = inifile.get('settings', 'pass')
login_url = "http://ssl.realworld.jp/auth/?site=service_navi_jp&goto=http%3A%2F%2Fmrga.service-navi.jp%2F"

driver = webdriver.Chrome('./chromedriver')
driver.get(login_url)
form = driver.find_elements_by_tag_name('form')[0]
for tag in form.find_elements_by_tag_name('input'):
	id = tag.get_attribute('id')
	if id == "rwsid":
		tag.send_keys(mail)
	elif id == "pass":
		tag.send_keys(passwd)

	type = tag.get_attribute('type')
	if type == 'submit':
		tag.submit()
		break

antena = driver.find_element_by_css_selector("div.antennaList")
a_list = antena.find_elements_by_tag_name("a")
links = []
for tag in a_list:
	href = tag.get_attribute('href')
	links.append(str(href))

print(len(links))
for link in links:
	print(link)
	driver.get(link)
	
	"""
	try:
		button = driver.find_element_by_css_selector("div.feature__button")
		span = button.find_element_by_css_selector("span.button--close")
		print("AD")
	except NoSuchElementException:
		print()
	"""

	ul_tag = driver.find_element_by_css_selector("ul.new__list")
	li_tag = ul_tag.find_elements_by_tag_name("li")[0]
	a_tag = li_tag.find_element_by_tag_name("a")
	href = a_tag.get_attribute('href')
	driver.get(href)

	sec = driver.find_element_by_css_selector("section.entrance")
	div_tag = sec.find_element_by_css_selector("div.button__layer")
	div_tag.find_element_by_tag_name("a").click()
	
	div_tag = tab_page.find_element_by_css_selector("div.article-read-more")
	a_tag = div_tag.find_element_by_tag_name("a")
	href = a_tag.get_attribute('href')
	driver.get(href)

driver.quit()