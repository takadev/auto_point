import sys
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Rlogin:

	BASE_PATH = '/Users/TK/project/auto_point/'
	CONFIG_INI = BASE_PATH + 'config.ini'
	DRIVER = BASE_PATH + 'chromedriver'
	AD_EXT = BASE_PATH + '3.15.0_0.crx'

	def __init__(self, login_url, section):
		self.login_url = login_url
		self.section = section

	def get_driver(self):
		chrome_options = Options()
		chrome_options.add_extension(self.AD_EXT)
		driver = webdriver.Chrome(self.DRIVER, chrome_options=chrome_options)
		sleep(15)
		if len(driver.window_handles) >= 2:
			driver.close()
			driver.switch_to.window(driver.window_handles[0])

		return driver

	def login(self, driver):
		inifile = configparser.SafeConfigParser()
		inifile.read(self.CONFIG_INI)

		driver.get(self.login_url)
		form = driver.find_elements_by_tag_name('form')[0]
		for tag in form.find_elements_by_tag_name('input'):
			id = tag.get_attribute('id')
			if id == "rwsid":
				tag.send_keys(inifile.get(self.section, 'id'))
			elif id == "pass":
				tag.send_keys(inifile.get(self.section, 'pass'))

			type = tag.get_attribute('type')
			if type == 'submit':
				tag.submit()
				break

		return driver
