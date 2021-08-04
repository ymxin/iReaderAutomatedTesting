#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/6/28 8:55 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_allure_demo.py
# @Project : iReaderAutomatedTesting

import allure


@allure.link("http://www.baidu.com", name='连接')
def test_with_link():
    print('这是一条加了连接的测试用例')


TEST_CASE_LINK = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9840828097459376277%22%7D&n_type=0&p_from=1'


@allure.link(TEST_CASE_LINK, '注册用例')
def test_with_link2():
    print('这是一条加了连接的测试用例222222')


# --allure-link-pattern=issue:http://www.baidu.com/issue/{}
@allure.issue('10', '这是一个issue')
def test_issue_link():
    assert 1 == 2

def test_attach_text():
    allure.attach("这是一个纯文本信息",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段HTML代码</body>","html测试",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("/Users/miaoxinyao/PycharmProjects/ymxProject/iReaderAutomatedTesting/practice_demo/pytest_demo/img.png",name="添加一个图片",attachment_type=allure.attachment_type.PNG)
