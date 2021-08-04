#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/3 5:15 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_feature_scope.py
# @Project : iReaderAutomatedTesting

import pytest

@pytest.fixture(scope='module')
def open():
    print("打开浏览器")
    yield
    print("关闭浏览器")

class TestSearch:

    def test_search1(self,open):
        print("test_search1")
        # 要想引发异常，最简单的形式就是输入关键字raise，后跟要引发的异常的名称。
        # 关键字raise是用来抛出异常的，一旦抛出异常后，后续的代码将无法运行。
        raise NameError

class TestSearch2:

    def test_search2(self,open):
        print("test_search2")

@pytest.mark.usefixtures('open')
def test_search():
    print("test_search3")
