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

	def test_1_9_Register_PC_註冊頁面_填寫錯誤身份證號(self):
		print('==========test_1_9_Register_PC_註冊頁面_填寫錯誤身份證號==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#第一階段註冊(電話、密碼、驗證碼)
		Register_stage_one(self)
		#姓名欄
		name_field=register_name_field(self)
		#身分證
		idCard_field=register_idCard_field(self)
		#email
		email_field=register_email_field(self)
		#完成開戶
		submitForm_button=register_submitForm_button(self)
		#隨機名字
		name=Chinese_name_generator()
		#隨機身分證
		idCard=random_pure_digits(self,18)
		name_field.send_keys(name)
		idCard_field.send_keys(idCard)
		email_field.send_keys('yoyododohoho@gmail.com')

		#提示字
		alert_text = self.browser.find_element_by_xpath('//*[@id="regForm"]/div[4]/span').text
		alert_text_expect = '身份证不正确！'
		if(alert_text == alert_text_expect):
			print('正確!跳出提示:',alert_text)
		else:
			print('錯誤!跳出提示:',alert_text)
			self.assertEqual(alert_text,alert_text_expect)
