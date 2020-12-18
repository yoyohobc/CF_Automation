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


	def test_1_06_Register_PC_註冊頁面_好友推薦過來的(self):
		print('==========test_1_06_Register_PC_註冊頁面_好友推薦過來的==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		print('點擊"好友推荐过来的？"')
		#好友推荐过来的？
		self.browser.find_element_by_xpath('//*[@id="submitForm"]/p').click()
		#推薦人手機號輸入框
		Recommender_watermark = self.browser.find_element_by_xpath('//*[@id="directRecommender"]').get_attribute("placeholder")

		Recommender_watermark_expect = '请输入推荐人手机号码'

		if(Recommender_watermark == Recommender_watermark_expect):
			print('正確!推薦人手機號輸入框顯示:',Recommender_watermark)
		else:
			print('錯誤!推薦人手機號輸入框顯示:',Recommender_watermark)
			self.assertEqual(Recommender_watermark,Recommender_watermark_expect)
