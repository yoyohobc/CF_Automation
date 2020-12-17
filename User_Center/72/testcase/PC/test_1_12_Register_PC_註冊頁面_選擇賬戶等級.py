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

	def test_1_12_Register_PC_註冊頁面_選擇賬戶等級(self):
		print('==========test_1_12_Register_PC_註冊頁面_選擇賬戶等級==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#第一階段註冊(電話、密碼、驗證碼)
		Register_stage_one(self)
		level_path = '/html/body/div[3]/div/div[1]/div[2]/div/a'
		#迷你
		MIN=self.browser.find_element_by_xpath(level_path+'[1]')
		#标准
		STD=self.browser.find_element_by_xpath(level_path+'[2]')
		#铂金
		PLA=self.browser.find_element_by_xpath(level_path+'[3]')
		#巴菲特级
		ZER=self.browser.find_element_by_xpath(level_path+'[4]')

		print('默認帳戶等級檢查')
		#帳戶等級被選擇時class會變active1
		STD_class_expect = 'active1'
		#抓標準帳戶的class
		STD_class = STD.get_attribute("class")
		if(STD_class == STD_class_expect):
			print('正確!帳戶等級默認是標準')
		else:
			print('錯誤!帳戶等級默認不是標準')
			self.assertEqual(STD_class,STD_class_expect)

		print('\n帳戶等級切換檢查')
		account_level=('迷你','標準','鉑金','巴菲特')
		elements=(MIN,STD,PLA,ZER)
		length = len(elements)
		#預期class同STD_class_expect
		element_class_expect = STD_class_expect
		for i in range(length):
			print('目前帳號切換為:',account_level[i])
			#點擊並抓取目前loop到的元素做比較
			elements[i].click()
			element_class=elements[i].get_attribute("class")
			if(element_class == element_class_expect):
				print('正確!帳戶等級切換為'+account_level[i])
			else:
				print('錯誤!帳戶等級沒有切換為'+account_level[i])
				self.assertEqual(element_class,element_class_expect)
