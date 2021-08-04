#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/8 8:48 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_ordering.py
# @Project : iReaderAutomatedTesting

import pytest


@pytest.mark.run(order=3)
def test_1():
    assert True

@pytest.mark.run(order=1)
def test_2():
    assert 1 == 1

@pytest.mark.run(order=2)
def test_3():
    assert 2 == 2
