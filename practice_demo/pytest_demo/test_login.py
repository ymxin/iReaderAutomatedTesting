#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/24 9:41 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_login.py
# @Project : iReaderAutomatedTesting
import pytest

def login(username):
    return username


@pytest.mark.login
def test_A():
    assert login('murcy') == 'murcy'

@pytest.mark.login
def test_B():
    print("我是，需要登录")


def test_C():
    assert 1 == 1

def test_D():
    print('我是D，无需登录')
