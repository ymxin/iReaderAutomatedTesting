#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/2 9:23 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_login2.py
# @Project : iReaderAutomatedTesting
import pytest

# 分别运行看下 scope：function、class、module、session
@pytest.fixture(scope="class")
def login():
    print("登录方法")
    username = 'admin'
    password = '123456'
    yield [username,password]
    print("退出登录")

class TestLogin:

    def test_login(self,login):
        print(f"用户的信息是：{login}")
        print("这是一条 test_login 用例")

    def test_login2(self,login):
        print("这是一条 test_login2 用例")
