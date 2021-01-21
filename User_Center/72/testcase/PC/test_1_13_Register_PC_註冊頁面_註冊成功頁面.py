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

	def test_1_13_Register_PC_註冊頁面_註冊成功頁面(self):
		print('==========test_1_13_Register_PC_註冊頁面_註冊成功頁面==========')
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
			print('正確!開戶訊息顯示:',success_text)
		else:
			print('錯誤!開戶訊息顯示:',success_text)
			self.assertEqual(success_text[8:],success_text_expect)
		#將帳號資訊寫入csv
		Write_account_information(success_text[:8],random_phone)
		#創富logo
		elements_expect = ('https://img.cfd139.com/source/www/template/logo-black.png', 'https://ac.cfd139.com/images/pc/pc-chenggong-img.jpg', '可用手机号或账号登录用户中心及交易平台', '当天注资，领 5000 美元赠金+现金红包！', '下载体验', '注资领赠金', '在线客服')
		elements=(('創富國際logo',self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/img').get_attribute("src")),
		('勾勾圖',self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/img').get_attribute("src")),
		('可用手机号或账号登录用户中心及交易平台',self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]').text),
		('当天注资，领 5000 美元赠金+现金红包！',self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[4]').text),
		('下载体验',self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[5]/a[1]').text),
		('注资领赠金',self.browser.find_element_by_xpath('//*[@id="activeBtn"]').text),
		('在线客服',self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/a').text))
		length = len(elements)
		for i in range(length):
			if(elements[i][1]==elements_expect[i]):
				print('正確!"'+elements[i][0]+'"顯示正確!')
			else:
				print('錯誤!"'+elements[i][0]+'"顯示錯誤!')
				self.assertEqual(elements[i][1],elements_expect[i])
