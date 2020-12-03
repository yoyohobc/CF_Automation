# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re, os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import Random
#用戶中心登入頁面
PC_URL = 'http://trader.will68.com/smartfx-pcusercenter/'
#開啟真實帳號
create_account_url = 'http://ac108.trexttd.com/registerPc.html'
#真實帳號註冊頁面
real_register_url = 'http://ac108.trexttd.com/registerNextPc.html'
random = Random()
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
