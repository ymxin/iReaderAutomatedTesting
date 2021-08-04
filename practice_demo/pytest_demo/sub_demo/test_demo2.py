#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/1 11:27 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_demo2.py
# @Project : iReaderAutomatedTesting

import pytest

# @pytest.fixture()
# def connectDB():
#     print("test_demo2 下的 connectDB ")

def test_a(connectDB):
    print("sub demo 下的 test_a")

class TestA():

    def test_b(self):
        print("sub demo 下的 test_b")