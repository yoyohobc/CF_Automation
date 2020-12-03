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


	def test_1_1_Register_PC(self):
		print('==========test_1_1_Register_PC_註冊頁面、各個元素檢查==========')
		browser = self.browser
		#登入頁面
		browser.get(PC_URL)
		time.sleep(2)
		#點擊還沒有帳號
		browser.find_element_by_xpath('//*[@id="supplementSubmi"]/div[4]/a[1]').click()
		time.sleep(2)
		title = browser.find_element_by_xpath('//*[@id="mian"]/div[2]/div/div').text
		if (title=='开启真实账户'):
			print('正確!开启真实账户顯示:',title)
		else:
			print('錯誤!开启真实账户顯示:',title)
			raise AssertionError('錯誤!开启真实账户顯示:',title)
		#註冊頁面元素檢查
		register_phone = browser.find_element_by_xpath('//*[@id="accountNumber"]')

		register_password = browser.find_element_by_id('thPassword')

		register_Verification = browser.find_element_by_id('msgCode')

		register_submit_button = browser.find_element_by_id('subAll')

		elements = [[register_phone,'電話欄'],[register_password,'密碼欄'],
		[register_Verification,'驗證碼欄'],[register_submit_button,'提交真實開戶按鈕']]
		for element in elements:
			try:
				element[0]
				print(element[1],"顯示正確!")
			except NoSuchElementException:
				print(element[1],"顯示錯誤!")
