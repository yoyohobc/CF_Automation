# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time, os
from Parameter import *
#from common.sendEmail import *  # For Mac, 記得改成 from command.sendEmail import *
#from common.uploadSlack import *   # For Mac, 記得改成 from command.uploadSlack import *
import coverage

# source指定的是待測程式所在資料夾名稱
# cov = coverage.coverage(config_file=True)
cov = coverage.coverage()
cov.start()


# 確認版本
if (device == 'mobile'):
    if (Browser =='Safari'):
        browser = webdriver.Safari()
        browser.set_window_position(0, 0)
        browser.set_window_size(375, 667)
    else:
        # 设置手机型号
        #mobileEmulation = {'deviceName': deviceName}
        options = webdriver.ChromeOptions()

        # 隱藏"Chrome is being controlled by automated software" Infobar
        # options.add_argument('disable-infobars') -- 無效
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # 隱藏視窗
        # options.add_argument('headless')

        options.add_experimental_option('mobileEmulation', mobileEmulation)

        # 启动driver
        # browser = webdriver.Chrome(chrome_options=options)
        browser = webdriver.Chrome(chrome_options = options)

else:
    if (Browser == 'Safari'):
        browser = webdriver.Safari()
    else:
        # browser = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        
        # 隱藏"Chrome is being controlled by automated software" Infobar
        # options.add_argument('disable-infobars') -- 無效
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
 
        # 隱藏視窗
        # options.add_argument('headless')

        browser = webdriver.Chrome(chrome_options=options)

if (deviceType == 'PC'):
    testcase_path = ".//testcase/PC"
else:
    testcase_path = ".//testcase/iPhone"

specific_testcase_path = './/testcase/SpecificTestCases'

def creat_suite():
    uit = unittest.TestSuite()
    #discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
    #discover = unittest.defaultTestLoader.discover(specific_testcase_path, pattern="test_*.py")
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_1_1*.py")

    for test_suite in discover:
        print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())

if (deviceType == 'PC'):
    if not os.path.exists('report/PC'):  os.makedirs('report/PC')
    reports_address = "report/PC/"
    report_path = "report/PC/" + now + ".html"
else:
    if not os.path.exists('report/PC'):  os.makedirs('report/PC')
    reports_address = "report/PC/"
    report_path = "report/PC/" + now + ".html"

suite = creat_suite()
file_results = open(report_path, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=file_results, title=u"108 用戶中心 PC",description=u"  執行環境: " + ' ' + OS + ' ' + Browser + ' ' + ' browser version: ' + browser.capabilities['browserVersion'] + ' driver version:' + browser.capabilities['chrome']['chromedriverVersion'][:14], verbosity=2)
# verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。
runner.run(suite)
file_results.close()

'''
the_last_report_address = SendEmail.acquire_report_address(reports_address)
SendEmail.send_email(the_last_report_address, now)
UploadSlack.file_upload(the_last_report_address, now)


cov.stop()
cov.save()
coveragePath = reports_address + '/Coverage/' + now + 'htmlcov'
cov.html_report(directory=coveragePath, omit=['BMW*', 'Parameter*', '*com*', 'HTML*', '__init__*', 'Dashboard*', 'Import*', 'Login*', 'QuickSearch*', 'Service*'])
'''
