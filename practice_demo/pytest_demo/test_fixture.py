#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/1 9:10 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_fixture.py
# @Project : iReaderAutomatedTesting
import pytest


# @pytest.fixture(autouse=True)
@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    username = 'cccccc'
    password = 'iiiiii'
    token= 'hnahnahnahna'
    # 激活fixture的teardown功能
    # yield 相当于return，返回数据可以直接跟在yield后面
    yield[username,password,token]
    print("注销操作")


def test_case1(login):
    # 获取fixture方法 的返回值，直接调用fixture方法
    print(f"用户的信息为：{login}")
    print("case1 需要登录操作")


def test_case2(connectDB):
    print("case2 不要登录操作")


def test_case3(connectDB):
    print("case3 不要登录操作")


@pytest.mark.usefixtures('login')
def test_case4():
    print("case4 要登录操作")
