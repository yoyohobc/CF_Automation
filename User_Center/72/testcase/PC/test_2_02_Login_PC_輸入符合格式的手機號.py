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

	def test_2_02_Login_PC_輸入符合格式的手機號(self):
		print('==========test_2_02_Login_PC_輸入符合格式的手機號==========')
		#登入頁面
		self.browser.get(PC_URL)
		#帳號欄、密碼欄、登入按鈕
		account_field,password_field,submit_button = login_elements(self)
		random_phone=random_phone_number(self)
		#輸入未註冊過的手機號登入、輸入已經註冊過的手機號登入
		inputs = (random_phone,registered_phone)
		for input in inputs:
			account_field.clear()
			account_field.send_keys(input)
			password_field.clear()
			password_field.send_keys('abc123')
			if(input==registered_phone):
				time.sleep(2)
				submit_button.click()
				time.sleep(2)
				#目前跳轉網址
				addressURL = self.browser.current_url
				#隱私政策網址
				addressURL_expect = 'https://cftrader.com/index.html'
				if(addressURL == addressURL_expect):
					print('正確!輸入已經註冊過的手機號登入至:',addressURL)
				else:
					print('錯誤!輸入已經註冊過的手機號登入至:',addressURL)
					self.assertEqual(addressURL,addressURL_expect)
			else:
				submit_button.click()
				time.sleep(1)
				#提示字檢查
				hint=self.browser.find_element_by_class_name('layui-layer-content').text
				hint_expect='账号或密码错误'
				if(hint==hint_expect):
					print('正確!輸入未註冊號碼登入時顯示:',hint)
				else:
					print('錯誤!輸入未註冊號碼登入時顯示:',hint)
					self.assertEqual(hint,hint_expect)
