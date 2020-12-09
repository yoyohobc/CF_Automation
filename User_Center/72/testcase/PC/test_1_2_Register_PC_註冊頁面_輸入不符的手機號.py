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


	def test_1_2_Register_PC_註冊頁面_輸入不符的手機號(self):
		print('==========test_1_2_Register_PC_註冊頁面_輸入不符的手機號==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#電話欄
		phone_filed = register_phone_field(self)
		#申請開戶鈕
		submitInfo_button = register_submitInfo_button(self)
		#低於11位手機號
		short_phone = random_phone_number(self,random.randint(1,7))
		#分別測試以下三種情況彈出的提示字
		actions=('輸入一個已經註冊的手機號，進行註冊','輸入一個低於11位手機號進行註冊','不輸入手機號，進行註冊')
		inputs = (registered_phone,short_phone,'')
		expect_result = ('您的手机已注册！请用手机号码登陆用户中心开通真实账户。如有疑问，请联系在线客服。',
		'请输入正确的手机号格式',
		'手机号码不能为空!')
		length = len(actions)
		for i in range(length):
			print('\n'+actions[i])
			phone_filed.clear()
			phone_filed.send_keys(inputs[i])
			submitInfo_button.click()
			time.sleep(1)
			print('目前輸入:',inputs[i])
			#抓提示字
			alert_text=self.browser.find_element_by_xpath('//*[@id="submitForm"]/div[2]/span').text
			if(alert_text==expect_result[i]):
				print('正確!出現提示:',alert_text)
			else:
				print('錯誤!出現提示:',alert_text)
				self.assertEqual(alert_text,expect_result[i])

		print('\n輸入一個大於11位手機號進行註冊')
		#大於11位手機號
		long_phone = random_phone_number(self,random.randint(9,17))
		phone_filed.clear()
		phone_filed.send_keys(long_phone)
		submitInfo_button.click()
		time.sleep(1)
		print('目前輸入:',long_phone)
		value_expect=long_phone[:11]
		value=phone_filed.get_attribute("value")
		if(value==value_expect):
			print('正確!輸入欄不顯示長度超出11的號碼:',value)
		else:
			print('錯誤!輸入欄顯示為:',value)
			self.assertEqual(value_expect,value)
