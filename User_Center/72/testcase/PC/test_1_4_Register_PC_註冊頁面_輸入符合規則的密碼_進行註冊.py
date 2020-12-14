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


	def test_1_4_Register_PC_註冊頁面_輸入符合規則的密碼_進行註冊(self):
		print('==========test_1_4_Register_PC_註冊頁面_輸入符合規則的密碼_進行註冊==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#電話欄
		phone_field = register_phone_field(self)
		#密碼欄
		password_field = register_password_field(self)
		#驗證碼欄位
		validatecode_field = register_validatecode_field(self)
		#申請開戶鈕
		submitInfo_button = register_submitInfo_button(self)
		#隨機電話號碼
		random_phone = random_phone_number(self)
		#獲取驗證碼API
		validate_code = register_account_api(self,random_phone)
		#輸入隨機手機
		phone_field.send_keys(random_phone)
		#輸入密碼
		password_field.send_keys('abc123')
		#輸入驗證碼
		validatecode_field.send_keys(validate_code)
		#申請開戶
		submitInfo_button.click()
		time.sleep(5)
		#檢查是否跳至補充資料頁面
		expect_url = 'https://ac.cfd139.com/cn/pc/rcfd_second?'
		currently_url = self.browser.current_url
		if(expect_url == currently_url):
			print('正確!輸入符合規則的密碼註冊時,可以跳轉至補充資料頁面')
		else:
			print('錯誤!輸入符合規則的密碼註冊時,無法跳轉至補充資料頁面')
			self.assertEqual(expect_url,currently_url)
