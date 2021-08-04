#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/9 9:23 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_allure.py
# @Project : iReaderAutomatedTesting

import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')