#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 10:21 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_demo.py
# @Project : iReaderAutomatedTesting
import requests
from jsonpath import jsonpath
from hamcrest import *


class TestDemo:

    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            'level': 1,
            'name': 'liming'
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)

        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'name': 'admin',
            'password': '123456'
        }
        r = requests.post("https://httpbin.testing-studio.com/post",data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            'name': 'admin',
            'password': '123456'
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['name'] == 'admin'

    def test_post_json2(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'

    def test_header(self):
        headers = {'user-agent':'myapp/0.0.1'}
        r = requests.get("https://httpbin.testing-studio.com/get", headers=headers)
        print(r.text)
        print(r.json())
        print(r.request)
        assert r.status_code == 200
        assert r.json()['headers']['User-Agent'] == 'myapp/0.0.1'

    def test_hamrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('开源项目'))

