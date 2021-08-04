#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/1 11:31 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : conftest.py
# @Project : iReaderAutomatedTesting

import pytest

@pytest.fixture(scope='session')
def connectDB():
    print("sub demo下的 connectDB 连接")
    yield
    print("关闭数据库")
