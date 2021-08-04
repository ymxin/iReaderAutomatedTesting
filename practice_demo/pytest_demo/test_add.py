#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/22 9:16 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_add.py
# @Project : iReaderAutomatedTesting
import pytest
import yaml


def add(x,y):
    return x + y

@pytest.mark.add
def test_add():
    assert add(1,2) == 3
    assert add(2,3) == 5
    assert add(10,2) == 12

class TestDemo:

    def test_demo(self):
        x = "hello world"
        print(f"{x} python")
        assert 'h' in x

    def test_demo2(self):
        x = 'hello'
        assert hasattr(x,"check")

    # def test_demo3(self):
    #     x = 4
    #     y = 4
    #     assert x == y
    #
    # def test_demo4(self):
    #     x = 1
    #     print(x)
    #     assert x == 2
    #
    # def test_demo5(self):
    #     assert 1 == 1

    @pytest.mark.parametrize('a',[1,2,3])
    @pytest.mark.parametrize('b',[4,5,6])
    def test_demo6(self,a,b):
        print(f'a={a},b={b}')

# 乘法运算
def sub(a,b):
    return a - b

with open('./datas/add.yaml') as f:
    datas = yaml.safe_load(f)['sub']
    sub_data = datas['datas']
    print(sub_data)
    myids = datas['myids']
    print(myids)


@pytest.mark.parametrize(
    'x,y,expect',sub_data,ids=myids
)
def test_sub(x,y,expect):
    result = sub(x,y)
    assert result == expect

@pytest.mark.parametrize("a,b,expect",[
    (1,2,3),
    (2,2,4)
])
def test_add_calc(a,b,expect):
    assert a + b == expect


