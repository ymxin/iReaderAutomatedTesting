#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/5 8:46 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_assert.py
# @Project : iReaderAutomatedTesting
import pytest


def test_assert():
    assert 'h' in 'hello'
    assert 7 > 6
    assert 1 == 1
    assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}

# 断言异常
def test_type_error():
    with pytest.raises(TypeError):
        '2' + 2

# 详细断言异常
def test_type_error2():
    with pytest.raises(TypeError) as exc:
        '2' + 2

    # 断言异常类型 type
    assert exc.type == TypeError
    # 断言异常 value 值
    assert "can only concatenate" in str(exc.value)

# 断言装饰器
@pytest.mark.xfail(raises=TypeError)
def test_type_error3():
    '2' + 2