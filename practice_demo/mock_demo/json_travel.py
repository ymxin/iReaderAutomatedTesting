#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 8:53 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : json_travel.py
# @Project : iReaderAutomatedTesting
import json


def json_travel(data):
    # 判断传入的数据类型{"a":{"b":{"c":1}}}
    if isinstance(data, dict):
        # 遍历字典的数据
        # 当是字典格式，递归value值
        for key, value in data.items():
            data[key] = json_travel(value)
    elif isinstance(data, list):
        # 当数据类型是list的时候，添加到结构内，并添加
        # 到结构内，并继续递归遍历，直到数据不为可迭代对象时
        # data_new = []
        # for value in data:
        #     data_new.append(json_travel(value))
        data = [json_travel(value) for value in data]
    elif isinstance(data, int) or isinstance(data, float):
        data = data * 1
    elif isinstance(data,bool):
        data = data
    elif isinstance(data, str):
        data = data + "a"
    else:
        data = data
    return data


if __name__ == "__main__":
    data = json.load(open("temp.json"), encoding='utf-8')
    # print(data)
    new_data = json_travel(data)
    with open('new.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, fp=f, indent=2,ensure_ascii=False)
