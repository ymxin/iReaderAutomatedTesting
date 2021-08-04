#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/8 8:02 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_rerun.py
# @Project : iReaderAutomatedTesting
from time import sleep

import pytest


def test_rerun1():
    sleep(0.5)
    assert 1 == 2

def test_rerun2():
    sleep(0.5)
    assert 2 == 2

@pytest.mark.flaky(reruns=2,reruns_delay=2)
def test_rerun3():
    sleep(0.5)
    assert 'h' == 'world'