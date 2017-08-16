import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Fsurvey%2F"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.get_driver_no_ext()
driver = rloginCls.login(driver)

ul_tag = driver.find_element_by_css_selector("ul#survey_wrap")
li_tags = ul_tag.find_elements_by_tag_name("li")
cm_links = []
gm_links = []
info_links = []
for tag in li_tags:
	a_tag = tag.find_element_by_tag_name("a")
	href = str(a_tag.get_attribute('href'))
	if href.find("cmstart") > -1:
		cm_links.append(href)
	elif href.find("gmostart") > -1:
		gm_links.append(href)
	elif href.find("infopanel") > -1:
		info_links.append(href)

for link in gm_links:
	print(link)
	driver.get(link)

	buttons = driver.find_elements_by_tag_name("button")
	if len(buttons) <= 0:
		continue

	input = None
	for button in buttons:
		type = button.get_attribute("type")
		if type == "submit":
			input = button
			break

	if input == None:
		continue

	driver.execute_script("arguments[0].click();", input)
	driver.switch_to.window(driver.window_handles[0])

	is_finish = False
	while True:
		if is_finish == True:
			break
		inputs = driver.find_elements_by_tag_name("input")
		if len(inputs) <= 0:
			break

		try:
			select = driver.find_element_by_tag_name("select")
			option = select.find_elements_by_tag_name("option")[1]
			select_element = Select(select)
			value = str(option.get_attribute('value'))
			select_element.select_by_value(value)
		except NoSuchElementException:
			pass

		inc_checkbox = False
		inc_raido = False
		for tag in inputs:
			type = tag.get_attribute("type")
			if type == "submit":
				driver.execute_script("arguments[0].click();", tag)
				break
			elif type == "button":
				if str(tag.get_attribute("name")).find("close") > -1:
					is_finish = True
			elif type == "radio" and inc_raido == False:
				driver.execute_script("arguments[0].click();", tag)
				inc_raido = True
			elif type == "checkbox" and inc_checkbox == False:
				driver.execute_script("arguments[0].click();", tag)
				inc_checkbox = True
			elif type == "text":
				try:
					if tag.text.find("歳") > -1:
						input.send_keys("28")
					else:
						input.send_keys("特になし")
				except NoSuchElementException:
					pass

		buttons = driver.find_elements_by_tag_name("button")
		try:
			for tag in buttons:

					type = tag.get_attribute("type")
					if type == "submit":
						driver.execute_script("arguments[0].click();", tag)
						driver.switch_to.window(driver.window_handles[0])
						break
		except TimeoutException:
			continue


driver.quit()
