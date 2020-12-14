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


	def test_1_8_Register_PC_註冊頁面_在線客服(self):
		print('==========test_1_8_Register_PC_註冊頁面_在線客服==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		print('點擊"在线客服"')
		#在线客服
		self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/a').click()
		time.sleep(2)
		#切換至最新開啟視窗
		self.browser.switch_to.window(self.browser.window_handles[-1])
		#目前跳轉網址
		addressURL = self.browser.current_url
		#在線客服網址
		addressURL_expect = 'https://www.cf-service.com/k800/chatClient/chatbox.jsp'

		if(addressURL[:54] == addressURL_expect):
			print('正確!目前頁面跳轉至:',addressURL)
		else:
			print('錯誤!目前頁面跳轉至:',addressURL)
			self.assertEqual(addressURL[:54],addressURL_expect)
