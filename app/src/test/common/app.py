#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/11 下午7:07
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : app.py
# @Project : iReaderAutomatedTesting
from appium import webdriver

from app.src.test.page.main_page import MainPage


class App:

    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps["platformName"] = 'android'
        caps['devicesName'] = 'emulator-5554'
        caps['appPackage'] = 'com.chaozh.iReaderFree'
        caps['appActivity'] = 'com.chaozh.iReader.ui.activity.WelcomeActivity'
        caps['noReset'] = 'true'
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

        # 隐式等待
        self.driver.implicitly_wait(10)

    def goto_main_page(self):
        '''
        进入到主界面
        :return:
        '''
        return MainPage(self.driver)
