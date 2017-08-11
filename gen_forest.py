import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Fforest%2F"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.get_driver_no_ext()
driver = rloginCls.login(driver)

article = driver.find_element_by_tag_name("article")
div_tags = article.find_elements_by_tag_name("div")
find = False
for tag in div_tags:
	try:
		a_tags = tag.find_elements_by_tag_name("a")
		for a_tag in a_tags:
			img_tags = a_tag.find_elements_by_tag_name("img")
			for img_tag in img_tags:
				src = img_tag.get_attribute('src')
				if str(src).find('star.gif') > -1:
					driver.execute_script("arguments[0].click();", a_tag)
					find = True
					break
			if find == True:
				break
		if find == True:
			break

	except NoSuchElementException:
		continue

forest = driver.find_element_by_css_selector("div#forestBox")
osusume = forest.find_element_by_css_selector("div#osusumemori")
boxes = osusume.find_elements_by_css_selector("div.osusume_box")
links = []
for tag in boxes:
	a_tag = tag.find_element_by_tag_name("a")
	links.append(str(a_tag.get_attribute('href')))

for link in links:
	print(link)
	driver.get(link)

driver.quit()