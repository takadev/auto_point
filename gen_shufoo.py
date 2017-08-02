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
login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Fshufoo"

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

target_tag = None
div_tags = driver.find_elements_by_tag_name("div")
for tag in div_tags:
	if str(tag.get_attribute("name")) == "area_based_list":
		target_tag = tag
		break

tag = target_tag.find_elements_by_css_selector("li.content_flyer")[0]
a_tag = tag.find_element_by_css_selector("a.btn_watch")
driver.get(str(a_tag.get_attribute("href")))
sleep(5)

driver.quit()