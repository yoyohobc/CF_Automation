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


	def test_1_5_Register_PC_註冊頁面_輸入驗證碼(self):
		print('==========test_1_5_Register_PC_註冊頁面_輸入驗證碼==========')
		#跳至註冊頁(Parameter)
		Jump_to_RegisterPage(self)
		#電話欄
		phone_field = register_phone_field(self)
		#密碼欄
		password_field = register_password_field(self)
		#驗證碼欄位
		validatecode_field = register_validatecode_field(self)
		#獲取驗證碼鈕
		validatecode_button = register_validatecode_button(self)
		#申請開戶鈕
		submitInfo_button = register_submitInfo_button(self)
		#隨機電話號碼
		random_phone = random_phone_number(self)
		#輸入隨機手機
		phone_field.send_keys(random_phone)
		#輸入密碼
		password_field.send_keys('abc123')
		#點擊獲取驗證碼
		time.sleep(1)
		validatecode_button.click()
		time.sleep(3)
		#檢查是否倒數開始
		secs = self.browser.find_element_by_xpath('//*[@id="secendhtml"]').text
		#是否有彈出滑動圖片驗證
		#是
		if(secs == ''):
			#標記為真時,在測試報表提示要再手動測試這項
			sixty_seconds_mark = True
			#關閉驗證
			self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[6]/div/div[2]/div/a[1]').click()
		#否
		else:
			#標記
			sixty_seconds_mark = False
			print('驗證碼正常進行60s倒數測試')
			#轉成數字
			int_secs = int(secs[:-1])
			#看60秒倒數是否誤差於五秒內
			if(55 <= int_secs <= 60):
				print('正確!驗證碼正常進行60s倒計時')
				print('驗證碼秒數顯示:',secs)
			else:
				print('錯誤!驗證碼未正常進行60s倒計時')
				print('驗證碼秒數顯示:',secs)
				raise AssertionError('錯誤!驗證碼未正常進行60s倒計時')
		#輸入錯誤驗證碼
		print('\n輸入錯誤驗證碼')
		wrong_code=random_pure_digits(self,4)
		validatecode_field.clear()
		validatecode_field.send_keys(wrong_code)
		submitInfo_button.click()
		print('目前輸入:',wrong_code)
		time.sleep(1)
		#提示字
		alert_text = self.browser.find_element_by_xpath('//*[@id="submitForm"]/div[7]/span').text
		alert_text_expect = '手机验证码不正确!'
		if(alert_text == alert_text_expect):
			print('正確!跳出提示:',alert_text)
		else:
			print('錯誤!跳出提示:',alert_text)
			self.assertEqual(alert_text,alert_text_expect)
		#大於四碼驗證碼
		print('\n驗證碼輸入大於四碼')
		long_code=random_pure_digits(self,random.randint(5,10))
		validatecode_field.clear()
		validatecode_field.send_keys(long_code)
		print('目前輸入:',long_code)
		value=validatecode_field.get_attribute("value")
		value_expect = long_code[:4]
		if(value == value_expect):
			print('正確!驗證碼欄顯示:',value)
		else:
			print('錯誤!驗證碼欄顯示:',value)
			self.assertEqual(value,value_expect)
		#標記為真時,在測試報表提示要再手動測試這項
		if(sixty_seconds_mark):
			raise AssertionError('驗證碼60s倒數計時,需再進行手動驗證,其他項目皆已通過')
