import sys
import random
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
login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Fsurvey%2F"

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

ul_tag = driver.find_element_by_css_selector("ul#survey_wrap")
li_tags = ul_tag.find_elements_by_tag_name("li")
links = []
for tag in li_tags:
	a_tag = tag.find_element_by_tag_name("a")
	links.append(str(a_tag.get_attribute('href')))

print(len(links))
for link in links:
	print(link)
	driver.get(link)
	sleep(1)

	input = driver.find_element_by_css_selector("input#btnlarge")
	driver.execute_script("arguments[0].click();", input)
	sleep(1)

	while True:
		questions = driver.find_elements_by_css_selector("div.question")
		for q in questions:

			try:
				select = q.find_element_by_tag_name("select")
				option = select.find_elements_by_tag_name("option")[1]
				select_element = Select(select)
				value = str(option.get_attribute('value'))
				select_element.select_by_value(value)
				continue
			except NoSuchElementException:
				pass

			input = q.find_element_by_tag_name("input")
			type = input.get_attribute("type")
			if type == "text":
				try:
					div_tag = q.find_element_by_css_selector("div.note")
					if div_tag.text.find("歳") > -1:
						input.send_keys("28")
					else:
						input.send_keys("特になし")
					continue
				except NoSuchElementException:
					pass

			elif type == "radio" or type == "checkbox":
				driver.execute_script("arguments[0].click();", input)

		matrixes = driver.find_elements_by_css_selector("div#answerMatrix")
		for matrix in matrixes:
			tbodies = matrix.find_elements_by_tag_name("tbody")

			print(len(tbodies))
			for tbody in tbodies:
				tr_tags = tbody.find_elements_by_tag_name("tr")
				checkbox = []
				radio = []
				inc_checkbox = False
				inc_raido = False
				for tr_tag in tr_tags:
					try:
						div_tags = tr_tag.find_elements_by_css_selector("div.matrix_answercell")
						for div_tag in div_tags:
							input = div_tag.find_element_by_tag_name("input")
							type = input.get_attribute("type")
							if type == "radio":
								inc_raido = True
							elif type == "checkbox":
								inc_checkbox = True

						if inc_raido != False or inc_checkbox != False:
							break
					except NoSuchElementException:
						pass

				if inc_raido == True and inc_checkbox == False:
					for tr_tag in tr_tags:
						try:
							div_tag = tr_tag.find_element_by_css_selector("div.matrix_answercell")
							input = div_tag.find_element_by_tag_name("input")
							driver.execute_script("arguments[0].click();", input)
						except NoSuchElementException:
							pass
				elif inc_raido == False and inc_checkbox == True:
					for tr_tag in tr_tags:
						try:
							if tr_tag.text.find("すべて") > -1:
								continue
							if tr_tag.text.find("あてはまるものはない") > -1:
								continue
								
							div_tags = tr_tag.find_elements_by_css_selector("div.matrix_answercell")
							div_len = len(div_tags)
							if div_len <= 0:
								continue

							input = div_tags[0].find_element_by_tag_name("input")
							driver.execute_script("arguments[0].click();", input)

						except NoSuchElementException:
							pass
						
				elif inc_raido == True and inc_checkbox == True:
					print("both")
					for tr_tag in tr_tags:
						try:
							div_tags = tr_tag.find_element_by_css_selector("div.matrix_answercell")
							for tag in dev_tags:
								input = tag.find_element_by_tag_name("input")
								driver.execute_script("arguments[0].click();", input)
							break
						except NoSuchElementException:
							pass

		try:
			div_tag = driver.find_element_by_css_selector("div#buttonArea")
			tags = div_tag.find_elements_by_tag_name("input")
			for tag in tags:
				if tag.get_attribute("value") == "次へ":
					driver.execute_script("arguments[0].click();", tag)
					sleep(1)
		except NoSuchElementException:
			break

driver.quit()
