import sys
import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2F?p=start"
mail = "nontan20xx@gmail.com"
passwd = "a4Gwfd8K"

driver = webdriver.Chrome('./chromedriver')
#driver = webdriver.Firefox()
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
survey_url = "http://www.gendama.jp/survey"
driver.get(survey_url)
surveys = driver.find_elements_by_css_selector("li.clearfix")
if len(surveys) > 0:
	atag = surveys[0].find_element_by_tag_name("a")
	driver.get(atag.get_attribute('href'))

	inputs = driver.find_elements_by_tag_name('input')
	for input in inputs:
		id = input.get_attribute('id')
		if id == "btnlarge":
			input.click()
			break
