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

	def test_2_01_Login_PC_登錄頁面元素檢查(self):
		print('==========test_2_01_Login_PC_登錄頁面元素檢查==========')
		#登入頁面
		self.browser.get(PC_URL)
		#帳號欄
		account_field = login_account_field(self)
		#密碼欄
		password_field = login_password_field(self)
		#登入按鈕
		submit_button = login_submit_button(self)
		#創富logo
		elements_expect = ('https://cftrader.com/dist/images/LOGO.png', 'https://cftrader.com/dist/images/login-text.png', '在线客服', '欢迎来到用户中心', '请输入账户/手机号', '请输入密码', '登录')
		elements=(('創富國際logo',self.browser.find_element_by_xpath('//*[@id="mian"]/div[1]/img[1]').get_attribute("src")),
		('文案圖',self.browser.find_element_by_xpath('//*[@id="mian"]/div[1]/img[2]').get_attribute("src")),
		('在线客服',self.browser.find_element_by_xpath('//*[@id="mian"]/div[3]/span/a').text),
		('用户中心標題',self.browser.find_element_by_xpath('//*[@id="mian"]/div[2]/div[1]').text),
		('帳號欄',account_field.get_attribute("placeholder")),
		('密碼欄',password_field.get_attribute("placeholder")),
		('登录鈕',submit_button.text))
		length = len(elements)
		for i in range(length):
			if(elements[i][1]==elements_expect[i]):
				print('正確!"'+elements[i][0]+'"顯示:',elements[i][1])
			else:
				print('錯誤!"'+elements[i][0]+'"顯示:',elements[i][1])
				self.assertEqual(elements[i][1],elements_expect[i])
