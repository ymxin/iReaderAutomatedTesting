#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 9:19 下午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : demo2.py
# @Project : iReaderAutomatedTesting

import json

from mitmproxy import ctx, http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow:http.HTTPFlow):
        # 判断是否是想要的请求信息，通过url判断
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.pretty_url:
            # 打开文件，读取文件数据，作为响应给返回。
            data = json.loads(flow.response.text)
            flow.response.text = json.dumps(self.json_travel(data))

    def json_travel(self,data):
        # 判断传入的数据类型{"a":{"b":{"c":1}}}
        if isinstance(data, dict):
            # 遍历字典的数据
            # 当是字典格式，递归value值
            for key, value in data.items():
                data[key] = self.json_travel(value)
        elif isinstance(data, list):
            # 当数据类型是list的时候，添加到结构内，并添加
            # 到结构内，并继续递归遍历，直到数据不为可迭代对象时
            # data_new = []
            # for value in data:
            #     data_new.append(json_travel(value))
            data = [self.json_travel(value) for value in data]
        elif isinstance(data, int) or isinstance(data, float):
            data = data * 2
        elif isinstance(data, bool):
            data = data
        elif isinstance(data, str):
            data = data
        else:
            data = data
        return data


addons = [
    Counter()
]

