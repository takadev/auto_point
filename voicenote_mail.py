import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep

inifile = configparser.SafeConfigParser()
inifile.read('./config.ini')
mail = inifile.get('voicenote', 'id')
passwd = inifile.get('voicenote', 'pass')
login_url = "http://www.voicenote.jp/"
url = "http://www.voicenote.jp/mypage/info.php"

driver = webdriver.Chrome('./chromedriver')
driver.get(login_url)

form = driver.find_element_by_tag_name('form')
for tag in form.find_elements_by_tag_name('input'):
	name = tag.get_attribute('name')
	if name == "login_email":
		tag.send_keys(mail)
	elif name == "login_pass":
		tag.send_keys(passwd)
	elif name == "login":
		tag.submit()
		break
try:
	tbody = driver.find_element_by_tag_name("tbody")
except NoSuchElementException:
	driver.quit()
	sys.exit()

tr_tags = tbody.find_elements_by_tag_name("tr")
links = []
for tag in tr_tags:
	if str(tag.get_attribute("class")) == "checked":
		continue

	try:
		a_tag = tag.find_element_by_tag_name("a")

		links.append(str(a_tag.get_attribute('href')))
	except NoSuchElementException:
		pass

for link in links:
	driver.get(link)
	sleep(1)

driver.quit()