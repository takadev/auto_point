import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

inifile = configparser.SafeConfigParser()
inifile.read('./config.ini')
mail = inifile.get('voicenote', 'id')
passwd = inifile.get('voicenote', 'pass')
login_url = "http://www.voicenote.jp/"

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

links = []
first = True
while True:
	ul_tag = driver.find_element_by_css_selector("ul.enquete-list")
	li_tags = ul_tag.find_elements_by_tag_name("li")
	for tag in li_tags:
		a_tag = tag.find_element_by_tag_name("a")
		links.append(str(a_tag.get_attribute('href')))

	break
	div_tag = driver.find_element_by_css_selector("div.pagination")
	if first == True:
		a_tag = div_tag.find_element_by_tag_name("a")
		driver.get(str(a_tag.get_attribute('href')))
		first = False
		sleep(1)
		continue

	a_tags = div_tag.find_elements_by_tag_name("a")
	if len(a_tags) <= 1:
		break

	driver.get(str(a_tags[1].get_attribute('href')))
	sleep(1)

for link in links:
	driver.get(link)
	sleep(1)

	while True:
		form = driver.find_element_by_tag_name("form")
		tbody = form.find_element_by_tag_name("tbody")
		tr_tags = tbody.find_elements_by_tag_name("tr")

		for tag in tr_tags:
			try:
				text = tag.find_element_by_tag_name("textarea")
				text.send_keys("特になし")
				continue
			except NoSuchElementException:
				pass
			try:
				input = tag.find_element_by_tag_name("input")
			except NoSuchElementException:
				continue

			type = input.get_attribute("type")
			if type == "radio" or type == "checkbox":
				driver.execute_script("arguments[0].click();", input)
				continue
	
		page = form.find_elements_by_css_selector("div.pagination")

		if len(page) > 0:
			a_tags = page[0].find_elements_by_tag_name("a")
			for a_tag in a_tags:
				if a_tag.text.find("次") > -1:
					driver.execute_script("arguments[0].click();", a_tag)
					sleep(1)
			continue
		else:
			conf = form.find_element_by_css_selector("input#confirm")
			driver.execute_script("arguments[0].click();", conf)
			sleep(1)

			form_tags = driver.find_elements_by_tag_name("form")
			for form in form_tags:
				name = form.get_attribute("name")
				if name == "form_complete":
					input = form.find_element_by_css_selector("input#complete")
					driver.execute_script("arguments[0].click();", input)
			
			sleep(1)
			break
	
driver.quit()