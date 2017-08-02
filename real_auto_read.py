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
login_url = "https://ssl.realworld.jp/auth?goto=http%3A%2F%2Frealworld.jp"
read_url = "http://realworld.jp/contents/rec"

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

driver.get(read_url)
sec = driver.find_element_by_css_selector("section#recommend")
a_list = sec.find_elements_by_tag_name("a")
links = []
cnt = 1
for tag in a_list:
	if cnt > 5:
		break
	cls = tag.get_attribute("class")
	if str(cls) == "":
		continue

	if str(cls).find('unable') > -1:
		continue

	href = tag.get_attribute('href')
	links.append(str(href))
	cnt += 1

for link in links:
	print(link)
	driver.get(link)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	sleep(1)
	try:
		sec_tag = driver.find_element_by_css_selector("section#complete")
		element = sec_tag.find_element_by_css_selector("a.modal-close")
		driver.execute_script("arguments[0].click();", element)
		sleep(1)
	except NoSuchElementException:
		pass

driver.quit()
