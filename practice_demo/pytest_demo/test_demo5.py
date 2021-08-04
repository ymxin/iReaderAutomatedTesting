#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/7 12:41 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_demo5.py
# @Project : iReaderAutomatedTesting

import pytest


def test_1():
    assert 1 + 1 == 2


def test_2():
    assert 100 + 100 == 200


def test_3():
    assert -1 + -2 == -3


@pytest.mark.parametrize('input_num,expect', [
    ('1+1', 2),
    ('-1+-1', -2),
    ('100+200', 300)
])
def test_4(input_num, expect):
    print(f"判断测试数据{input_num}是否符合预期{expect}")
    assert eval(input_num) == expect


def test_5():
    print(eval('2'))
    print(eval("1"))
    print(eval("'hello world'"))


# @pytest.mark.parametrize(["name", "pwd"], [("yy1", "123"), ("yy2", "123")])
# @pytest.mark.parametrize(("name", "pwd"), [("yy1", "123"), ("yy2", "123")])
# @pytest.mark.parametrize("name,pwd", [("yy1", "123"), ("yy2", "123")])

@pytest.mark.parametrize(['test_input', 'expect'], [
    ('1+1', 2),
    ('2+2', 4)
])
def test_6(test_input, expect):
    assert eval(test_input) == expect


@pytest.mark.parametrize(('test_input', 'expect'), [
    ('-1+-1', -2),
    ('0.1+0.1', 0.2)
],ids=['negative','float'])
def test_7(test_input, expect):
    assert eval(test_input) == expect

@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[4,5,6,7])
def test_8(a,b):
    print(f'a+b={a}+{b}')

# 字典
data_1 = (
    {
        'user': 1,
        'pwd': 2
    },
    {
        'user': 3,
        'pwd': 4
    }
)

@pytest.mark.parametrize('dic', data_1)
def test_9(dic):
    print(f'测试数据为\n{dic}')
    print(f'user:{dic["user"]},pwd:{dic["pwd"]}')

# 增加可读性
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

# 重要！！！！！！！！！！
# ids
ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]


@pytest.mark.parametrize('a, b, expect', data_1, ids=ids)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2数据为{}-{}'.format(a, b))
        assert a + b == expect
