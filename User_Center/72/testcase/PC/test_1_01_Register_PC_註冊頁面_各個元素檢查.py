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


	def test_1_01_Register_PC_註冊頁面_各個元素檢查(self):
		print('==========test_1_01_Register_PC_註冊頁面、各個元素檢查==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#檢查頁面字段
		check_eles =[['在线客服','/html/body/div[1]/div/div[2]/a'],
		['创富 CFD 真实账户','/html/body/div[2]/div/div/h1'],
		['手机号码','//*[@id="submitForm"]/div[1]/label'],
		['自设密码','//*[@id="submitForm"]/div[3]/label'],
		['手机验证码','//*[@id="submitForm"]/div[5]/label'],
		['申请开户','//*[@id="submitInfo"]'],
		['获取验证码','//*[@id="submitForm"]/div[5]/a[1]']]
		for ele in check_eles:
			#預期字段
			expect = ele[0]
			#結果
			result = self.browser.find_element_by_xpath(ele[1]).text

			if (expect == result):
				print(ele[0],'顯示正確')
			else:
				print('錯誤!',ele[0],'顯示:',result)
				self.assertEqual(expect,result)
				raise AssertionError('錯誤!',ele[0],'顯示:',result)
