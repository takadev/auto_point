import sys
import configparser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Rlogin:

	CONFIG_INI = '/Users/TK/project/auto_point/config.ini'

	def __init__(self, login_url, section):
		self.login_url = login_url
		self.section = section

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
