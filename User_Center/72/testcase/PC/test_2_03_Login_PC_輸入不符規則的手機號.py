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

	def test_2_03_Login_PC_輸入不符規則的手機號(self):
		print('==========test_2_03_Login_PC_輸入不符規則的手機號==========')
		#登入頁面
		self.browser.get(PC_URL)
		#帳號欄、密碼欄、登入按鈕
		account_field,password_field,submit_button = login_elements(self)
		actions = ('輸入錯誤的手機號，進行登錄','輸入小於11手機號','輸入大於11手機號','輸入未註冊的賬號','輸入低於八位的賬號','輸入大於八位的賬號')
		hints_expect = ('','','','','','')
		length = len(actions)
		for i in range(length):
			#提示字檢查
			hint=self.browser.find_element_by_class_name('//*[@id="accountNumber-error"]').text
			if(hint==hints_expect[i]):
				print('正確!'+actions[i]+'時顯示:',hint)
			else:
				print('錯誤!'+actions[i]+'時顯示:',hint)
				self.assertEqual(hint,hints_expect[i])
