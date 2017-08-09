import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

login_url = "http://ssl.realworld.jp/auth/?site=monow_jp&goto=http%3A%2F%2Fmonow.jp%2F&control=http%3A%2F%2Fmonow.jp%2Frws_session"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.get_driver()
driver = rloginCls.login(driver)

ul_tag = driver.find_element_by_css_selector("ul#timeline")
items = ul_tag.find_elements_by_tag_name("li")

links = []
cnt = 1
for item in items:
	if cnt > 10:
		break
	atag = item.find_element_by_tag_name("a")
	href = atag.get_attribute('href')
	links.append(str(href))
	cnt += 1

for link in links:
	print(link)
	driver.get(link)
	try:
		monow_point = driver.find_element_by_css_selector("a.monowBt_point")
	except NoSuchElementException:
		continue

	driver.execute_script("arguments[0].click();", monow_point)

driver.quit()