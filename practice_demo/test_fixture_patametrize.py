#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 12:17 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_fixture_patametrize.py
# @Project : iReaderAutomatedTesting

import pytest

# 方法名作为参数
test_user_data = ['Jenny', 'Liming']

@pytest.fixture(scope="module")
def login_r(request):
    # 通过request.param 获取参数
    user = request.param
    print(f"登录用户:{user}")
    return user

@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""


