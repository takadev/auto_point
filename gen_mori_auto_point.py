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

forest_url = "http://www.gendama.jp/forest/"
driver.get(forest_url)

forest = driver.find_element_by_css_selector("div#forestBox")
div_tags = forest.find_elements_by_tag_name("div")
for tag in div_tags:
	if str(tag.get_attribute('id')) != "":
		continue
	if str(tag.get_attribute('class')) != "":
		continue

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