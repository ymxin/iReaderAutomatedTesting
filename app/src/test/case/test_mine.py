#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/20 下午10:56
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_mine.py
# @Project : iReaderAutomatedTesting
from app.src.test.common.app import App


class TestMine:

    def setup(self):
        self.app = App()

    def test_mine(self):
        self.app.goto_main_page().goto_mine_page()
        assert '1>2'
