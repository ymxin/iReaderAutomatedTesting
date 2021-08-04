#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/28 8:31 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_oauth.py
# @Project : iReaderAutomatedTesting
import requests
from requests.auth import HTTPBasicAuth

class TestOauth:

    def test_oauth(self):

        r = requests.get(url='https://httpbin.testing-studio.com/basic-auth/admin/123',
                         auth=HTTPBasicAuth('admin','123'))
        print(r)
