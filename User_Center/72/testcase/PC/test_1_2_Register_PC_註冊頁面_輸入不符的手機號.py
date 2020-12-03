import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
	    # create a new Browser session
	    setUpBrowser(self)
	    #隱性等待10秒
		self.browser.implicitly_wait(10)
	    print(" -- set up finished -- ")

	def tearDown(self):
	    self.browser.quit()
	    print('-- tear down finished -- ')


	def test_1_2_Register_PC_註冊頁面_輸入不符的手機號(self):
		print('==========test_1_2_Register_PC_註冊頁面_輸入不符的手機號==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)

		#註冊頁面、輸入一個已經註冊的手機號，進行註冊
		registered_phone
		#註冊頁面、輸入一個低於11位手機號進行註冊
		#註冊頁面、輸入一個大於11位手機號進行註冊
		#註冊頁面、不輸入手機號，進行註冊
