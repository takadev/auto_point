import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Frace"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.get_driver()
driver = rloginCls.login(driver)

try:
	div_tag = driver.find_element_by_css_selector("div#race_simple05")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)
except NoSuchElementException:
	pass

sleep(1)
try:
	div_tag = driver.find_element_by_css_selector("div#race_simple01")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)
except NoSuchElementException:
	pass

sleep(1)
try:
	div_tag = driver.find_element_by_css_selector("div#race_simple02")
	element = div_tag.find_element_by_tag_name("a")
	driver.execute_script("arguments[0].click();", element)
except NoSuchElementException:
	pass

sleep(1)
driver.quit()