#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/1 11:49 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_params.py
# @Project : iReaderAutomatedTesting

import pytest
@pytest.fixture(params=[1,2,3])
def login1(request):
    data= request.param
    print("获取数据")
    return data

def test_case(login1):
    print(login1)
    print("测试用例1")
