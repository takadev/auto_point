import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

inifile = configparser.SafeConfigParser()
inifile.read('./config.ini')
mail = inifile.get('settings', 'id')
passwd = inifile.get('settings', 'pass')
url = "http://monow.jp/"
login_url = "http://ssl.realworld.jp/auth/?site=monow_jp&goto=http%3A%2F%2Fmonow.jp%2F&control=http%3A%2F%2Fmonow.jp%2Frws_session"

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


ul_tag = driver.find_element_by_css_selector("ul#timeline")
items = ul_tag.find_elements_by_tag_name("li")

links = []
for item in items:
	atag = item.find_element_by_tag_name("a")
	href = atag.get_attribute('href')
	links.append(str(href))

for link in links:
	print(link)
	driver.get(link)
	try:
		monow_point = driver.find_element_by_css_selector("a.monowBt_point")
	except NoSuchElementException:
		continue

	monow_point.click()
