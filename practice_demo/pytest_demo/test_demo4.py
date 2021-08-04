#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/7 9:00 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_demo4.py
# @Project : iReaderAutomatedTesting
import pytest


def test_function():
    n = 1
    while True:
        print(f"这是我第{n}条用例")
        n += 1
        if n == 5:
            pytest.skip("我跑五次了不跑了")