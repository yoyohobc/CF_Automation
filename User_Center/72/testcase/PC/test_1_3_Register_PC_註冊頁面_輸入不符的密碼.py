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


	def test_1_3_Register_PC_註冊頁面_輸入不符的密碼(self):
		print('==========test_1_3_Register_PC_註冊頁面_輸入不符的密碼==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#密碼欄
		password_field = register_password_field(self)
		#申請開戶鈕
		submitInfo_button = register_submitInfo_button(self)
		#純符號
		symbols=generate_random_symbols(self,random.randint(5,16))
		#低於五位數密碼
		short_password=generate_random_password(self,random.randint(1,4))
		#純字母5-16位
		letters = random_pure_letters(self,random.randint(5,16))
		#純數字5-16位
		digits = random_pure_digits(self,random.randint(5,16))
		#分別測試以下三種情況彈出的提示字
		actions=('輸入一個不符合規則的密碼，進行註冊','輸入低於5位的密碼，進行註冊','輸入純數字的密碼，進行註冊','輸入純字母的密碼，進行註冊')
		#輸入
		inputs = (symbols,short_password,digits,letters)
		#預期提示字
		expect_result = '密码为5-16位字符，必须包含字母和数字!'
		length = len(actions)
		for i in range(length):
			print('\n'+actions[i])
			password_field.clear()
			password_field.send_keys(inputs[i])
			submitInfo_button.click()
			time.sleep(1)
			print('目前輸入:',inputs[i])
			#抓提示字
			alert_text=self.browser.find_element_by_xpath('//*[@id="submitForm"]/div[4]/span').text
			if(alert_text==expect_result):
				print('正確!出現提示:',alert_text)
			else:
				print('錯誤!出現提示:',alert_text)
				self.assertEqual(alert_text,expect_result)
