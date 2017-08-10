import sys
import rlogin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep

login_url = "https://ssl.realworld.jp/auth/?site=gendama_jp&rid=&af=&frid=&token=&goto=http%3A%2F%2Fwww.gendama.jp%2Fcmkuji%2F"
rloginCls = rlogin.Rlogin(login_url, "settings")
driver = rloginCls.get_driver_no_ext()
driver = rloginCls.login(driver)

cm_url = "http://dreevee.com/ad_areas/8c28c899e286798e685427c3a20d08c3338c70eb/ad_frames/video"

driver.get(cm_url)
div_tags = driver.find_elements_by_css_selector("div.col-dv-container-horizontal")

links = []
for tag in div_tags:
	try:
		a_tag = tag.find_element_by_tag_name("a")
		span_tag = a_tag.find_element_by_css_selector("span.point-movie")
		if span_tag.text.find("pt") > -1:
			links.append(str(a_tag.get_attribute('href')))
	except NoSuchElementException:
		pass
	
for link in links:
	print(link)
	driver.get(link)
	actions = ActionChains(driver)
	div_tag = driver.find_element_by_css_selector("div.container-video-player")
	video = div_tag.find_element_by_css_selector("div.load_videoplayer")
	a_tag = video.find_element_by_css_selector("a.injection-video-player")
	# driver.execute_script("arguments[0].click();", a_tag)
	actions.move_to_element(a_tag).click().perform()
	sleep(1)
	
	end_tag = div_tag.find_element_by_css_selector("a.end_videoplayer")
	count = end_tag.find_element_by_css_selector("p.countdown")
	span = count.find_element_by_css_selector("span#countdown-seconds")

	while True:
		if str(span.get_attribute('innerHTML')).find("20") <= -1:
			actions.move_to_element(a_tag)
			actions.move_by_offset(10, 10).click().perform()
			sleep(5)
			break
	
driver.quit()	