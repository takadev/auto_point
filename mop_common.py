import sys
import rlogin
from selenium import webdriver

class Common:

	def init(self, ext = True):
		login_url = "https://ssl.pc.moppy.jp/login/"
		rloginCls = rlogin.Rlogin(login_url, "moppi")
		if ext == True:
			driver = rloginCls.get_driver()
		else:
			driver = rloginCls.get_driver_no_ext()
		driver = rloginCls.login_mop(driver)

		return driver
