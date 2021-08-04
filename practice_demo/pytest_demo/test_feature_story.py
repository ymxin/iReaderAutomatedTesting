#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/28 8:37 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_feature_story.py
# @Project : iReaderAutomatedTesting
import allure
@allure.feature('登录模块')
class TestFeature:
    @allure.story('登录成功')
    def test_login_success(self):
        print('登录成功')

    @allure.story('登录失败')
    def test_login_fail(self):
        print('登录失败')
        assert 1 == '1'

    @allure.story('输入错误的用户名')
    def test_login_username(self):
        print('输入用户名')
        assert 1 == 2

    @allure.story('输入错误的密码')
    def test_login_password(self):
        print('输入密码')
        assert not 1

    @allure.story('输入用户名、密码，登录成功')
    def test_login_user_pass(self):
        with allure.step('点击用户名'):
           print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        print('点击登录')
        with allure.step('登录成功'):
            print('登录成功啦~')


