import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

inifile = configparser.SafeConfigParser()
inifile.read('/Users/TK/project/auto_point/config.ini')
mail = inifile.get('settings', 'id')
passwd = inifile.get('settings', 'pass')
login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Fforest%2F"

driver = webdriver.Chrome('/Users/TK/project/auto_point/chromedriver')
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

div_tags = driver.find_elements_by_tag_name("div")
for tag in div_tags:
	try:
		a_tag = tag.find_element_by_tag_name("a")
		img_tag = a_tag.find_element_by_tag_name("img")
		src = img_tag.get_attribute('src')
		if str(src).find('star.gif') == -1:
			continue

		driver.execute_script("arguments[0].click();", a_tag)
		break

	except NoSuchElementException:
		continue

forest = driver.find_element_by_css_selector("div#forestBox")
osusume = forest.find_element_by_css_selector("div#osusumemori")
boxes = osusume.find_elements_by_css_selector("div.osusume_box")
links = []
for tag in boxes:
	a_tag = tag.find_element_by_tag_name("a")
	links.append(str(a_tag.get_attribute('href')))

for link in links:
	print(link)
	driver.get(link)

driver.quit()