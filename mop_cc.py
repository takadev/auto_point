import sys
import mop_common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = mop_common.Common().init()
url = "http://pc.moppy.jp/cc/"
driver.get(url)

div_tag = driver.find_element_by_css_selector("div.main")
li_tags = div_tag.find_elements_by_tag_name("li")
links = []
for tag in li_tags:
	a_tag = tag.find_element_by_tag_name("a")
	links.append(str(a_tag.get_attribute('href')))

for link in links:
	print(link)
	driver.get(link)
	sleep(0.5)

driver.quit()