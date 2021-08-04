#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/11 下午7:07
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : base_page.py
# @Project : iReaderAutomatedTesting
from typing import List, Dict

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import yaml


class BasePage:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 查找元素
    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    # 点击
    def find_click(self,by,locator):
        self.find(by,locator).click()

    # 输入元素
    def find_send(self,by,locator,key):
        self.find(by,locator).send_keys(key)

    # 滑动点击
    def swipe_click(self,text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));'
                                 ).click()

    def parse_action(self,path,fun_name):
        with open(path,"r",encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]

        for step in steps:

            if step["action"]=="find_click":
                self.find_click(step["by"],step["locator"])
            elif step["action"]=="find":
                self.find(step["by"],step["locator"])
            elif step["action"]=="find_send":
                self.find_send(step["action"],step["locator"],step["key"])
            elif step["action"]=="swipe_click":
                self.swipe_click(step["text"])


