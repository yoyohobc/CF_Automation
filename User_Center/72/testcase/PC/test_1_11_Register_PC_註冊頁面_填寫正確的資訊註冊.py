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

	def test_1_11_Register_PC_註冊頁面_填寫正確的資訊註冊(self):
		print('==========test_1_11_Register_PC_註冊頁面_填寫正確的資訊註冊==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#第一階段註冊(電話、密碼、驗證碼)
		random_phone = Register_stage_one(self)
		#白名單API
		register_whitelist_api(self,random_phone)
		#隨機名字
		name=Chinese_name_generator()
		#隨機產生身分證(id_number_util.identity)
		random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
		idCard = IdNumber.generate_id(random_sex)
		#填入欄位並送出
		#第二階段註冊(姓名、身分證、電郵)
		Register_stage_two(self,name,idCard)

		#註冊成功訊息檢查
		success_text_expect = '真实账号注册成功'
		success_text=self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]').text
		if(success_text[8:]==success_text_expect):
			print('正確!填寫正確的身份證號、姓名、郵箱號註冊後顯示:',success_text)
		else:
			print('錯誤!填寫正確的身份證號、姓名、郵箱號註冊失敗')
			self.assertEqual(success_text[8:],success_text_expect)
		#將帳號資訊寫入csv
		Write_account_information(success_text[:8],random_phone)
