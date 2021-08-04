#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 11:30 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_yaml.py
# @Project : iReaderAutomatedTesting

import pytest
import yaml

@pytest.mark.parametrize("a,b", yaml.safe_load(open("./datas/data.yaml",encoding='utf-8')))
def test_yaml(a,b):
    print(f"a + b = {a + b}")

