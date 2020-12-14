# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re, os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from random import Random
import requests
import string
import json
#用戶中心登入頁面PRD
PC_URL = 'https://cftrader.com/'
#開啟真實帳號
create_account_url = 'https://ac.cfd139.com/cn/pc/rcfd_account'
#真實帳號註冊頁面
real_register_url = 'http://ac108.trexttd.com/registerNextPc.html'
random = Random()
#已註冊手機
registered_phone = '18856818076'
# 指定OS
OS = 'Windows'
#OS = 'Mac'

# 指定測試設備
device = 'PC'
#device = ''
#deviceType = 'PC'
deviceType = 'PC'
mobileEmulation = {
    #'deviceName' : 'iPhone 6'
    #'deviceName' : 'PC Mini'
    'deviceName': 'PC'
}
if (device == 'mobile'):
    width = '375'
    height = '667'
else:
    print('無長寬設定')

# 指定瀏覽器
Browser = 'Chrome'
#Browser = 'Safari'
#consol log 設定
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }


def setUpBrowser(self,language='zh-tw'):
    if (device == 'mobile'):
        if (Browser == 'Safari'):
            self.browser = webdriver.Safari()
            self.browser.set_window_position(0, 0)
            self.browser.set_window_size(width, height)
        else:
            # 设置手机型号
            # self.mobileEmulation = {'deviceName': deviceName}
            self.options = webdriver.ChromeOptions()

            # 隱藏"Chrome is being controlled by automated software" Infobar
            # options.add_argument('disable-infobars') -- 無效
            self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
            self.options.add_experimental_option('useAutomationExtension', False)
            #語言 zh-tw en
            self.options.add_argument('--lang='+language)

            # 隱藏視窗
            # self.options.add_argument('headless')

            self.options.add_experimental_option('mobileEmulation', mobileEmulation)

            # 启动driver
            self.browser = webdriver.Chrome(chrome_options=self.options,desired_capabilities=d)
    else:
        if (Browser == 'Safari'):
            self.browser = webdriver.Safari()
        else:
            # self.browser = webdriver.Chrome()

            self.options = webdriver.ChromeOptions()

            # 隱藏"Chrome is being controlled by automated software" Infobar
            # self.options.add_argument('disable-infobars') -- 無效
            self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
            self.options.add_experimental_option('useAutomationExtension', False)
            #語言 zh-tw en
            self.options.add_argument('--lang='+language)

            # 隱藏視窗
            # self.options.add_argument('headless')

            self.browser = webdriver.Chrome(chrome_options=self.options,desired_capabilities=d)
def Random_String_Number(self,length):
    chars = '0123456789'
    random_numbers = ''
    for j in range(length):
        random_numbers+=chars[random.randint(0,len(chars) - 1)]
    return random_numbers

def Jump_to_RegisterPage(self):
    #登入頁面
    self.browser.get(PC_URL)
    #點擊還沒有帳號
    self.browser.find_element_by_xpath('//*[@id="supplementSubmi"]/div[4]/a[1]').click()
    #切換至最新開啟視窗
    self.browser.switch_to.window(self.browser.window_handles[-1])
#第一階段註冊(電話、密碼、驗證碼)
def Register_stage_one(self):
    #電話欄
    phone_field = register_phone_field(self)
    #密碼欄
    password_field = register_password_field(self)
    #驗證碼欄位
    validatecode_field = register_validatecode_field(self)
    #申請開戶鈕
    submitInfo_button = register_submitInfo_button(self)
    #隨機電話號碼
    random_phone = random_phone_number(self)
    #獲取驗證碼API
    validate_code = register_account_api(self,random_phone)
    #輸入隨機手機
    phone_field.send_keys(random_phone)
    #輸入密碼
    password_field.send_keys('abc123')
    #輸入驗證碼
    validatecode_field.send_keys(validate_code)
    #申請開戶
    submitInfo_button.click()
#手機欄位
def register_phone_field(self):
    return self.browser.find_element_by_xpath('//*[@id="phone"]')
#密碼欄位
def register_password_field(self):
    return self.browser.find_element_by_xpath('//*[@id="upwd"]')
#驗證碼欄位
def register_validatecode_field(self):
    return self.browser.find_element_by_xpath('//*[@id="yanZ"]')
#申請開戶
def register_submitInfo_button(self):
    return self.browser.find_element_by_xpath('//*[@id="submitInfo"]')
#獲取驗證碼按鈕
def register_validatecode_button(self):
    return self.browser.find_element_by_xpath('//*[@id="submitForm"]/div[5]/a[1]')
#姓名欄
def register_name_field(self):
    return self.browser.find_element_by_xpath('//*[@id="uname"]')
#身分證
def register_idCard_field(self):
    return self.browser.find_element_by_xpath('//*[@id="idCard"]')
#email
def register_email_field(self):
    return self.browser.find_element_by_xpath('//*[@id="email"]')
#完成開戶
def register_submitForm_button(self):
    return self.browser.find_element_by_xpath('//*[@id="submitForm"]')

def Chinese_name_generator():
    ch_name = ''
    for i in range(3):
        ch_name += chr(random.randint(0x4e00, 0x9fbf))
    return ch_name
#隨機產生電話
def random_phone_number(self,length=8):
	area_list = ['130', '131', '132', '133', '134', '135', '136', '137',
	'138', '139', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159','188','189']
	numbers = '0123456789'
	random_phone = random.choice(area_list)
	for i in range(length):
		random_phone+=numbers[random.randint(0,9)]
	return random_phone
#純字母
def random_pure_letters(self,length=8):
    letters=''
    for i in range(length):
        letters+=random.choice(string.ascii_letters)
    return letters
#純數字
def random_pure_digits(self,length=8):
    digits=''
    for i in range(length):
        digits+=random.choice(string.digits)
    return digits

#隨機產生符號
def generate_random_symbols(self,length=8):
	chars = '/*-+=-(){}[]\#$%^&*!~`,.?/"_"|<>;:'
	chars_length = len(chars) - 1
	random_symbols = ''
	for i in range(length):
		random_symbols+=chars[random.randint(0,chars_length)]
	return random_symbols

#隨機產生密碼
def generate_random_password(self,length=8):
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqstuvwxyz0123456789'
	chars_length = len(chars) - 1
	random_password = ''
	for i in range(length-1):
		random_password+=chars[random.randint(0,chars_length)]
	random_password+=random.choice(string.digits)
	return random_password
#獲取驗證碼API
def register_account_api(self,random_phone):
    request_url = "https://office.cf139.com/ValidateCodeLog/createValidateNo"

    payload = random_phone
    headers = {
      'Connection': 'close',
      'authority': 'office.cf139.com',
      'accept': 'application/json, text/plain, */*',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
      'content-type': 'application/json;charset=UTF-8',
      'origin': 'https://office.cf139.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://office.cf139.com/home/validater/validateNo',
      'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      'cookie': 'lang_type=0; JSESSIONID=84871DBC50AD6CCE38923B5F4F7FC5DF; cf88_id="user:763:869480c1-ce0e-4232-9a65-65b9336b2cec"'
    }

    response = requests.request("POST", request_url, headers=headers, data = payload,verify = False)
    #print(response.text.encode('utf8'))
    data = response.json()
    #回傳驗證碼
    return data['data']
