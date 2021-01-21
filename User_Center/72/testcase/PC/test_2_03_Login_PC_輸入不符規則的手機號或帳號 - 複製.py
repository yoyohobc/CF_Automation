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

	def test_2_03_Login_PC_輸入不符規則的手機號或帳號(self):
		print('==========test_2_03_Login_PC_輸入不符規則的手機號或帳號==========')
		#登入頁面
		self.browser.get(PC_URL)
		#帳號欄、密碼欄、登入按鈕
		account_field,password_field,submit_button = login_elements(self)
		#錯誤的手機號
		wrong_phone = random_pure_letters(self)
		#小於11手機號
		short_phone = random_phone_number(self,random.randint(0,7))
		#大於11手機號
		long_phone =  random_phone_number(self,random.randint(9,20))
		#低於八位的賬號
		pure_digits = random_pure_digits(self,random.randint(0,4))
		short_account = '811' +  pure_digits
		#輸入
		inputs = (wrong_phone,short_phone,long_phone,short_account)
		#行為描述
		actions = ('輸入錯誤的手機號，進行登錄','輸入小於11手機號','輸入大於11手機號','輸入低於八位的賬號')
		#預期結果
		result_expect = ('请输入正确的手机号','请输入正确的手机号',long_phone[:11],'请输入正确的交易账户')
		length = len(actions)
		for i in range(length):
			account_field.clear()
			account_field.send_keys(inputs[i])
			print('\n目前輸入:'+inputs[i])
			if(actions[i]=='輸入大於11手機號'):
				#帳號欄值檢查
				account_value = account_field.get_attribute("value")
				if(account_value==result_expect[i]):
					print('正確!'+actions[i]+'時帳號欄顯示:',account_value)
				else:
					print('錯誤!'+actions[i]+'時帳號欄顯示:',account_value)
					self.assertEqual(account_value,result_expect[i])
			else:
				#提示字檢查
				hint=self.browser.find_element_by_xpath('//*[@id="accountNumber-error"]').text
				if(hint==result_expect[i]):
					print('正確!'+actions[i]+'時顯示:',hint)
				else:
					print('錯誤!'+actions[i]+'時顯示:',hint)
					self.assertEqual(hint,result_expect[i])

				if(actions[i]=='輸入小於11手機號'):
					password_field.send_keys('abc123')
					submit_button.click()
					time.sleep(2)
					#目前跳轉網址
					addressURL = self.browser.current_url
					#預期網址(停留在登入頁)
					addressURL_expect = PC_URL
					if(addressURL == addressURL_expect):
						print('正確!'+actions[i]+'登入時停留在登入頁')
					else:
						print('錯誤!'+actions[i]+'登入時頁面跳轉至:',addressURL)
						self.assertEqual(addressURL,addressURL_expect)
					password_field.clear()

