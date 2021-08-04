#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/11 下午7:04
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : main_page.py
# @Project : iReaderAutomatedTesting
from app.src.test.common.base_page import BasePage


class MainPage(BasePage):

    def goto_bookshelf_page(self):
        '''
        进入到书架页面
        :return:
        '''
        pass

    def goto_bookstore_page(self):
        '''
        进入到书城页面
        :return:
        '''
        pass

    def goto_category_page(self):
        '''
        进入到分类页面
        :return:
        '''
        pass

    def goto_mine_page(self):
        '''
        进入到我的页面
        :return:
        '''
        self.parse_action("../../../data/main_page.yaml","goto_mine_page")