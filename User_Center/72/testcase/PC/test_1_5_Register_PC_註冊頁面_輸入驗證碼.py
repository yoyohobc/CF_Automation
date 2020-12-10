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
	    #self.browser.quit()
	    print('-- tear down finished -- ')


	def test_1_5_Register_PC_註冊頁面_輸入驗證碼(self):
		print('==========test_1_5_Register_PC_註冊頁面_輸入驗證碼==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#電話欄
		phone_field = register_phone_field(self)
		#密碼欄
		password_field = register_password_field(self)
		#驗證碼欄位
		validatecode_field = register_validatecode_field(self)
		#獲取驗證碼鈕
		validatecode_button = register_validatecode_button(self)
		#隨機電話號碼
		random_phone = random_phone_number(self)
		#輸入隨機手機
		phone_field.send_keys(random_phone)
		#輸入密碼
		password_field.send_keys('abc123')
		#點擊獲取驗證碼
		time.sleep(1)
		validatecode_button.click()
		time.sleep(2)
		#檢查是否倒數開始
		secs = self.browser.find_element_by_xpath('//*[@id="secendhtml"]').text
		#轉成數字
		int_secs = int(secs[:-1])
		#看60秒倒數是否誤差於五秒內
		if(55 <= int_secs <= 60):
			print('正確!驗證碼正常進行60s倒計時')
			print('驗證碼秒數顯示:',secs)
		else:
			print('錯誤!驗證碼未正常進行60s倒計時')
			print('驗證碼秒數顯示:',secs)
			raise AssertionError('錯誤!驗證碼未正常進行60s倒計時')
