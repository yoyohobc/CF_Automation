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


	def test_1_2_Register_PC(self):
		print('==========test_1_2_Register_PC_註冊頁面、點擊開立真實賬號，切換到真實賬號註冊頁面==========')
		browser = self.browser
		#真實帳號註冊頁面
		browser.get(real_register_url)
		time.sleep(3)
		#檢查頁面元素
		check_eles =[['迷你','//*[@id="mian"]/div[2]/div/div[2]/ul/li[1]'],
		['标准','//*[@id="mian"]/div[2]/div/div[2]/ul/li[2]'],
		['金钻','//*[@id="mian"]/div[2]/div/div[2]/ul/li[3]'],
		['请输入您的真实姓名 *','//*[@id="supplementSubmi"]/div/div[1]/div/div/div[1]/div'],
		['因监管要求，请输入您的真实身份证号码 *','//*[@id="supplementSubmi"]/div/div[2]/div/div/div[1]/div'],
		['账户的重要信息将发送到您的邮箱 *','//*[@id="supplementSubmi"]/div/div[3]/div/div/div[1]/div'],
		['提交真实开户','//*[@id="subAll"]']]
		for ele in check_eles:
			expect = ele[0]
			result = browser.find_element_by_xpath(ele[1]).text

			if (expect == result):
				print(ele[0],'顯示正確')
			else:
				print('錯誤!',ele[0],'顯示:',result)
				raise AssertionError('錯誤!',ele[0],'顯示:',result)

