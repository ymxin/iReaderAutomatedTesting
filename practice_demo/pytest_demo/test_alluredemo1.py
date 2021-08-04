#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/28 8:49 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_alluredemo1.py
# @Project : iReaderAutomatedTesting
import allure
import pytest

@allure.severity(allure.severity_level.BLOCKER)
@allure.title("成功测试用例标题")
def test_success():
    """this test succeeds"""
    assert True

@allure.severity(allure.severity_level.TRIVIAL)
@allure.description("""
这是一个模拟失败的测试用例
""")
def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

@allure.severity(allure.severity_level.BLOCKER)
def test_broken():
    raise Exception('oops')

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("多个参数{name},{phone},{age}")
@pytest.mark.parametrize("name,phone,age", [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
def test_test_test(name, phone, age):
    print(name, phone, age)

TEST_CASE_LINK = 'http://allure.qatools.ru/'

@allure.severity(allure.severity_level.MINOR)
@allure.link('https://www.baidu.com')
def test_with_link():
    pass

@allure.severity(allure.severity_level.NORMAL)
@allure.link('https://www.baidu.com', name='访问百度链接')
def test_with_named_link():
    pass

@allure.severity(allure.severity_level.NORMAL)
@allure.issue('140', 'bug issue链接')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, '测试用例地址')
def test_with_testcase_link():
    pass