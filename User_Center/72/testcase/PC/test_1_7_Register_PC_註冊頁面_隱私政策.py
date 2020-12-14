import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
		# create a new Browser session
		setUpBrowser(self)
		#隱性等待10秒
		self.browser.implicitly_wait(10)
		time.sleep(1)
		print(" -- set up finished -- ")

	def tearDown(self):
	    time.sleep(1)
	    self.browser.quit()
	    print('-- tear down finished -- ')


	def test_1_7_Register_PC_註冊頁面_隱私政策(self):
		print('==========test_1_7_Register_PC_註冊頁面_隱私政策==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		print('點擊"创富国际的隐私政策"')
		#创富国际的隐私政策。
		self.browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[3]/a').click()
		time.sleep(2)
		#切換至最新開啟視窗
		self.browser.switch_to.window(self.browser.window_handles[-1])
		#目前跳轉網址
		addressURL = self.browser.current_url
		#隱私政策網址
		addressURL_expect = 'https://img.cfd139.com/source/material/privacyPolicy.html'

		if(addressURL == addressURL_expect):
			print('正確!目前頁面跳轉至:',addressURL)
		else:
			print('錯誤!目前頁面跳轉至:',addressURL)
			self.assertEqual(addressURL,addressURL_expect)
