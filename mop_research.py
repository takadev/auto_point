import sys
import mop_common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = mop_common.Common().init()
search_url = "http://pc.moppy.jp/point_research/"
driver.get(search_url)

section_tag = driver.find_element_by_css_selector("section.pointResearch__box")
a_tags = section_tag.find_elements_by_tag_name("a")
links = []
for tag in a_tags:
	links.append(str(tag.get_attribute('href')))

for link in links:
	print(link)
	driver.get(link)

	try:
		sec_tag = driver.find_element_by_css_selector("section.ui-main-lower")
		a_tags = sec_tag.find_elements_by_tag_name("a")
		for tag in a_tags:
			if str(tag.get_attribute("class")).find("ui-button") > -1:
				driver.execute_script("arguments[0].click();", tag)
				break
	except NoSuchElementException:
		pass

	is_finish = False
	while True:
		if is_finish == True:
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

		try:
			form = driver.find_element_by_tag_name('form')
		except NoSuchElementException:
			is_finish = True
			continue

		for input in form.find_elements_by_tag_name('input'):
			type = input.get_attribute("type")
			if type == "submit":
				driver.execute_script("arguments[0].click();", input)
				break
			elif type == "radio" and is_raido == False:
				driver.execute_script("arguments[0].click();", input)
				is_raido = True
			elif type == "checkbox" and is_checkbox == False:
				driver.execute_script("arguments[0].click();", input)
				is_checkbox = True
			elif type == "button":
				driver.execute_script("arguments[0].click();", input)
				is_finish = True
				break
	

driver.quit()