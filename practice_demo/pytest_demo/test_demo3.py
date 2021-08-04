#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/7 8:52 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_demo3.py
# @Project : iReaderAutomatedTesting

import pytest

@pytest.fixture(autouse=True)
def login():
    print("====登录====")


def test_case01():
    print("我是测试用例11111")


@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_case02():
    print("我是测试用例22222")


class Test1:

    def test_1(self):
        print("%% 我是类测试用例1111 %%")

    @pytest.mark.skip(reason="这条用例不用执行，还需优化")
    def test_2(self):
        print("%% 我是类测试用例2222 %%")


@pytest.mark.skip(reason="类也可以跳过不执行")
class TestSkip:
    def test_1(self):
        print("%% 不会执行 TestSkip %%")
