import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome('/Users/TK/project/auto_point/chromedriver')
login_url = "http://ssl.realworld.jp/auth/?site=service_navi_jp&goto=http%3A%2F%2Fmrga.service-navi.jp%2Fsquare%2Farticles"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.login(driver)

antena = driver.find_element_by_css_selector("div.enquete_box")
a_list = antena.find_elements_by_tag_name("a")
links = []
for tag in a_list:
	href = tag.get_attribute('href')
	links.append(str(href))

bouns_url = ""
find_bouns = False
for link in links:
	print(link)
	driver.get(link)
	try:
		ul_tag = driver.find_element_by_css_selector("ul.new__list")
	except NoSuchElementException:
		continue
		
	li_tags = ul_tag.find_elements_by_tag_name("li")
	if len(li_tags) <= 0:
		continue

	if find_bouns == False:
		bouns_tag = li_tags[1].find_element_by_tag_name("a")
		if bouns_tag.text.find("ボーナス") > -1:
			bouns_url = bouns_tag.get_attribute('href')
			find_bouns = True

	li_tag = li_tags[0]
	a_tag = li_tag.find_element_by_tag_name("a")
	href = a_tag.get_attribute('href')
	driver.get(href)

	sec = driver.find_element_by_css_selector("section.entrance")
	div_tag = sec.find_element_by_css_selector("div.button__layer")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)

	driver.switch_to.window(driver.window_handles[1])
	try:
		div_tag = driver.find_element_by_css_selector("div.article")
		airtcle = div_tag.find_element_by_css_selector("div.article-read-more")
		a_tag = airtcle.find_element_by_tag_name("a")
		href = a_tag.get_attribute('href')
		driver.get(href)
	except NoSuchElementException:
		pass

	driver.close()
	driver.switch_to.window(driver.window_handles[0])

if find_bouns == True:
	driver.get(bouns_url)
	sec = driver.find_element_by_css_selector("section.entrance")
	div_tag = sec.find_element_by_css_selector("div.button__layer")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)

driver.quit()
