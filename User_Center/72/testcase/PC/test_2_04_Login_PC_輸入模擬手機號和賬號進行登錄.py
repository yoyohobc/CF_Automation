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

	def test_2_04_Login_PC_輸入模擬手機號和賬號進行登錄(self):
		print('==========test_2_04_Login_PC_輸入模擬手機號和賬號進行登錄==========')
		#登入頁面
		self.browser.get(PC_URL)
		#帳號欄、密碼欄、登入按鈕
		account_field,password_field,submit_button = login_elements(self)
		#輸入
		inputs = (demo_account,demo_phone)
		password = 'abc123'
		#行為描述
		actions = ('輸入模擬手機號進行登錄','輸入模擬賬號進行登錄')
		#預期結果
		#result_expect = ('请输入正确的手机号','请输入正确的手机号',long_phone[:11],'请输入正确的交易账户')
		length = len(actions)
		for i in range(length):
			account_field.clear()
			account_field.send_keys(inputs[i])
			password_field.clear()
			password_field.send_keys(password)
			submit_button.click()
			time.sleep(1)
			#提示字檢查
			hint=self.browser.find_element_by_class_name('layui-layer-content').text
			hint_expect='账号或密码错误'
			if(hint==hint_expect):
				print('正確!'+actions[i]+'時顯示:',hint)
			else:
				print('錯誤!'+actions[i]+'時顯示:',hint)
				self.assertEqual(hint,hint_expect)
			

