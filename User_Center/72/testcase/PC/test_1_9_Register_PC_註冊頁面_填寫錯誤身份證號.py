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
		#隨機名字
		name=Chinese_name_generator()
		#隨機身分證
		idCard=random_pure_digits(self,18)
		#填入欄位並送出
		#第二階段註冊(姓名、身分證、電郵)
		Register_stage_two(self,name,idCard)

		#提示字
		alert_text = self.browser.find_element_by_xpath('//*[@id="regForm"]/div[4]/span').text
		alert_text_expect = '身份证不正确！'
		if(alert_text == alert_text_expect):
			print('正確!跳出提示:',alert_text)
		else:
			print('錯誤!跳出提示:',alert_text)
			self.assertEqual(alert_text,alert_text_expect)
