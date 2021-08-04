#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/8 8:32 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_assume.py
# @Project : iReaderAutomatedTesting
import pytest


def test_assume():
    # assert 1 == 2
    # assert False == True
    # assert 100 == 200
    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
    pytest.assume(4 != 1)
