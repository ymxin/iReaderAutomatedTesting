#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/27 8:20 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_requests1.py
# @Project : iReaderAutomatedTesting


import requests

def test_demo():
    url = 'https://httpbin.testing-studio.com/cookies'
    header = {'User-Agent': 'user-agent'}
    cookie_data = {'cookie':'hello,cookie',
                   'pass':'123456'
                   }

    r = requests.get(url=url, headers = header, cookies=cookie_data)

    print(r.request.headers)