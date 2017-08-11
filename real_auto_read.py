import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

login_url = "https://ssl.realworld.jp/auth?goto=http%3A%2F%2Frealworld.jp"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.get_driver()
driver = rloginCls.login(driver)

read_url = "http://realworld.jp/contents/rec/page/"
page = 1
links = []
cnt = 1
while True:
	if cnt > 5 or page > 30:
		break

	read_page_url = read_url + str(page)
	driver.get(read_page_url)
	sec = driver.find_element_by_css_selector("section#recommend")
	a_list = sec.find_elements_by_tag_name("a")

	for tag in a_list:
		if cnt > 5:
			break
		cls = tag.get_attribute("class")
		if str(cls) == "":
			continue

		if str(cls).find('unable') > -1:
			continue

		if str(cls).find('clearfix') <= -1:
			continue

		href = tag.get_attribute('href')
		links.append(str(href))
		cnt += 1
	page += 1


for link in links:
	print(link)
	driver.get(link)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	sleep(1)
	try:
		sec_tag = driver.find_element_by_css_selector("section#complete")
		element = sec_tag.find_element_by_css_selector("a.modal-close")
		driver.execute_script("arguments[0].click();", element)
		sleep(1)
	except NoSuchElementException:
		pass

driver.quit()
