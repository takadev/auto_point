import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep

inifile = configparser.SafeConfigParser()
inifile.read('/Users/TK/project/auto_point/config.ini')
mail = inifile.get('settings', 'id')
passwd = inifile.get('settings', 'pass')
login_url = "http://ssl.realworld.jp/auth/?site=service_navi_jp&goto=http%3A%2F%2Fmrga.service-navi.jp%2F"
survey_url = "http://mrga.service-navi.jp/square/surveys"
colum_url = "http://mrga.service-navi.jp/square/columns"

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

driver.get(survey_url)
div_tag = driver.find_element_by_css_selector("div.enqueteBox")
a_tags = div_tag.find_elements_by_tag_name("a")
links = []
for tag in a_tags:
	links.append(str(tag.get_attribute('href')))

for link in links:
	sleep(1)
	driver.get(link)
	sleep(1)
	driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
	div_tag = driver.find_element_by_css_selector("div.attention")
	p_tag = div_tag.find_elements_by_tag_name("p")[1]
	span_tag = p_tag.find_element_by_tag_name("span")
	q_num = int(span_tag.text.replace("問", ""))

	cnt = 0
	while True:
		if cnt > q_num + 1:
			break
		try:
			select = driver.find_element_by_tag_name("select")
			option = select.find_elements_by_tag_name("option")[1]
			select_element = Select(select)
			value = str(option.get_attribute('value'))
			select_element.select_by_value(value)
		except NoSuchElementException:
			pass

		is_raido = False
		is_checkbox = False
		form = driver.find_elements_by_tag_name('form')[0]
		for tag in form.find_elements_by_tag_name('input'):
			type = tag.get_attribute('type')
			if type == 'submit':
				tag.submit()
				break
			elif type == 'radio' and is_raido == False:
				driver.execute_script("arguments[0].click();", tag)
				is_raido = True
			elif type == 'checkbox' and is_checkbox == False:
				driver.execute_script("arguments[0].click();", tag)
				is_checkbox = True

		cnt += 1

driver.get(colum_url)
div_tag = driver.find_element_by_css_selector("div.enqueteBox")
a_tags = div_tag.find_elements_by_tag_name("a")
links = []
for tag in a_tags:
	links.append(str(tag.get_attribute('href')))

for link in links:
	sleep(1)
	driver.get(link)
	sleep(1)

	skip = False
	for var in [1,2,3]:
		sleep(1)
		forms = driver.find_elements_by_tag_name('form')
		if len(forms) <= 0:
			skip = True
			break

		for tag in forms[0].find_elements_by_tag_name('input'):
			type = tag.get_attribute('type')
			if type == 'image':
				driver.execute_script("arguments[0].click();", tag)
				break

	if skip == True:
		break

	div_tag = driver.find_element_by_css_selector("div.now_column")
	span_tag = div_tag.find_element_by_css_selector("span.now_back")
	str_num = span_tag.text.replace("ただいま", "")
	num = int(str_num.replace("ページ中1ページ目", ""))

	for var in range(num):
		sleep(1)
		div_tag = driver.find_elements_by_css_selector("div.column_back_next_bt")[1]
		form = div_tag.find_element_by_tag_name('form')
		for tag in form.find_elements_by_tag_name('input'):
			type = tag.get_attribute('type')
			if type == 'image':
				driver.execute_script("arguments[0].click();", tag)
				break

	div_tag = driver.find_element_by_css_selector("div#pointget_bt")
	form = div_tag.find_element_by_tag_name('form')
	for tag in form.find_elements_by_tag_name('input'):
			type = tag.get_attribute('type')
			if type == 'image':
				driver.execute_script("arguments[0].click();", tag)
				break

	sleep(1)
	div_tag = driver.find_element_by_css_selector("div.now_column")
	span_tag = div_tag.find_element_by_css_selector("span.now_back")
	str_num = span_tag.text.replace("ただいま", "")
	num = int(str_num.replace("問中1問目", ""))


	for var in range(num):
		sleep(1)
		form = driver.find_element_by_tag_name('form')
		is_raido = False
		is_checkbox = False
		for tag in form.find_elements_by_tag_name('input'):
			type = tag.get_attribute('type')
			if type == 'submit':
				tag.submit()
				break
			elif type == 'radio' and is_raido == False:
				driver.execute_script("arguments[0].click();", tag)
				is_raido = True
			elif type == 'checkbox' and is_checkbox == False:
				driver.execute_script("arguments[0].click();", tag)
				is_checkbox = True

	div_tag = driver.find_element_by_css_selector("div#pointget_bt")
	form = div_tag.find_element_by_tag_name('form')
	for tag in form.find_elements_by_tag_name('input'):
			type = tag.get_attribute('type')
			if type == 'image':
				driver.execute_script("arguments[0].click();", tag)
				break

	sleep(1)
	div_tag = driver.find_element_by_css_selector("div#again_bt")
	a_tag = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", a_tag)

driver.quit()
