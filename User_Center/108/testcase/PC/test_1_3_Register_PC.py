import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
	    # create a new Browser session
	    setUpBrowser(self)
	    time.sleep(1)
	    print(" -- set up finished -- ")

	def tearDown(self):
	    time.sleep(1)
	    self.browser.quit()
	    print('-- tear down finished -- ')


	def test_1_3_Register_PC(self):
		print('==========test_1_3_Register_PC_註冊頁面-手機號錯誤提示==========')
		browser = self.browser
		#開啟真實帳號頁面
		browser.get(create_account_url)
		time.sleep(1)

		#手機號欄位
		phone_field = browser.find_element_by_id('accountNumber')
		#驗證按鈕
		verify_button = browser.find_element_by_id('second')
		#註冊頁面、輸入一個已經註冊的手機號，進行註冊 15124741343(暫時無法)
		#註冊頁面、輸入一個低於11位手機號進行註冊
		lower_than_eleven = Random_String_Number(self,random.randint(0,10))
		#註冊頁面、輸入一個大於11位手機號進行註冊
		higher_than_eleven = Random_String_Number(self,random.randint(12,20))
		
		check_list = [['輸入一個低於11位手機號進行註冊',lower_than_eleven,'请输入正确的手机号码'],['不輸入手機號，進行註冊','','请输入手机号码']]
		for check in check_list:
			print(check[0])
			phone_field.clear()
			phone_field.send_keys(check[0])
			verify_button.click()
			time.sleep(1)
			error_result = browser.find_element_by_id('accountNumber-error').text
			if(error_result == check[2]):
				print('正確!提示顯示:',error_result)
			else:
				print('錯誤!提示顯示:',error_result)
				raise AssertionError('錯誤!提示顯示:',error_result)
		phone_field.clear()
		phone_field.send_keys(higher_than_eleven)
		time.sleep(1)
		print(phone_field.text)
