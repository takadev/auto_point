import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = webdriver.Chrome('/Users/TK/project/auto_point/chromedriver')
login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fmrga.service-navi.jp%2Fsquare%2Fvotes"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.login(driver)
sleep(1)

div_tag = driver.find_element_by_css_selector("div.enquete_box")
a_tags = div_tag.find_elements_by_tag_name("a")
links = []
for tag in a_tags:
	links.append(str(tag.get_attribute('href')))

for link in links:
	print(link)
	try:
		driver.get(link)
	except TimeoutException:
		pass

	div_tag = driver.find_element_by_css_selector("div.start__inner")
	a_tags = div_tag.find_elements_by_tag_name("a")
	for tag in a_tags:
		if tag.get_attribute('class') == "start__button":
			driver.execute_script("arguments[0].click();", tag)
			break

	while True:
		try:
			form = driver.find_element_by_tag_name('form')
		except NoSuchElementException:
			break

		is_raido = False
		is_checkbox = False
		
		try:
			input_tags = form.find_elements_by_tag_name('input')
		except StaleElementReferenceException:
			break

		for tag in input_tags:
			try:
				type = tag.get_attribute('type')
			except StaleElementReferenceException:
				continue

			if type == 'submit':
				try:
					tag.submit()
				except TimeoutException:
					break
				break
			elif type == 'radio' and is_raido == False:
				driver.execute_script("arguments[0].click();", tag)
				is_raido = True
			elif type == 'checkbox' and is_checkbox == False:
				driver.execute_script("arguments[0].click();", tag)
				is_checkbox = True
			elif type == 'button':
				try:
					val = str(tag.get_attribute('value'))
				except StaleElementReferenceException:
					continue

				if val.find('投票') > -1:
					driver.execute_script("arguments[0].click();", tag)
					sleep(1)
					driver.switch_to.window(driver.window_handles[0])

					div_tag = driver.find_element_by_css_selector("div.button__box")
					tag = div_tag.find_element_by_tag_name("a")
					driver.execute_script("arguments[0].click();", tag)
					break

driver.quit()