#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/8 12:41 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_repeat.py
# @Project : iReaderAutomatedTesting
from time import sleep

import pytest

# def test_example():
#     import random
#     flag = random.choice([True, False])
#     print(flag)
#     sleep(1)
#     assert flag
#
# # pytest -s --count 5 -x 13repeat.py
#
# @pytest.mark.repeat(5)
# def test_repeat():
#     sleep(1)
#     print("测试用例执行")

class TestRepeat:

    def test_repeat1(self):
        print("test1++++++++test1")

    def test_repeat2(self):
        print("test2+++++++++test2")


class TestRepeat2:

    def test_repeat3(self):
        print("test3++++++++test3")

    def test_repeat4(self):
        print("test4+++++++++test4")

# pytest -s --count=2 --repeat-scope=class 13repeat.py