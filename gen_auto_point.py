import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

inifile = configparser.SafeConfigParser()
inifile.read('./config.ini')
mail = inifile.get('settings', 'id')
passwd = inifile.get('settings', 'pass')
login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2F?p=start"

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

sleep(1)
forest_url = "http://www.gendama.jp/forest/"
driver.get(forest_url)
sec = driver.find_element_by_css_selector("section.article")
ul_tag = sec.find_element_by_tag_name("ul")
li_tags = ul_tag.find_elements_by_tag_name("li")

links = []
for tag in li_tags:
	a_tag = tag.find_element_by_tag_name("a")
	links.append(str(a_tag.get_attribute('href')))

for link in links:
	driver.get(link)
	ul_tag = driver.find_element_by_css_selector("ul.new__list")
	li_tag = ul_tag.find_elements_by_tag_name("li")[0]
	a_tag = li_tag.find_element_by_tag_name("a")
	driver.get(a_tag.get_attribute('href'))
