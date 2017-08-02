import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

inifile = configparser.SafeConfigParser()
inifile.read('./config.ini')
mail = inifile.get('settings', 'id')
passwd = inifile.get('settings', 'pass')
login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Frace"

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

try:
	div_tag = driver.find_element_by_css_selector("div#race_simple05")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)
except NoSuchElementException:
	pass

sleep(1)
try:
	div_tag = driver.find_element_by_css_selector("div#race_simple01")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)
except NoSuchElementException:
	pass

sleep(1)
try:
	div_tag = driver.find_element_by_css_selector("div#race_simple02")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)
except NoSuchElementException:
	pass

sleep(1)
driver.quit()