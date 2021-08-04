#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/1 10:11 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : conftest.py
# @Project : iReaderAutomatedTesting

import pytest

@pytest.fixture(scope='session')
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")
