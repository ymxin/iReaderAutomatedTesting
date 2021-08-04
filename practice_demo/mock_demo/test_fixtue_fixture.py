#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 12:36 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_fixtue_fixture.py
# @Project : iReaderAutomatedTesting

import pytest

@pytest.fixture()
def connectDB():
    return "name,school"

@pytest.fixture()
def login(connectDB):
    return [connectDB]

def test_string(login):
    pass

@pytest.fixture()
def one():
    return 'one'

@pytest.fixture()
def two():
    return 2

@pytest.fixture()
def three(one,two):
    return [one, two]

@pytest.fixture()
def four():
    return ['one',2,3.0]

def test_five(four,three):
    three.append(3.0)

    assert three == four
