#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/23 8:54 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_mock.py
# @Project : iReaderAutomatedTesting

"""Send a reply from the proxy without sending any data to the remote server."""


# 修改response的值
import json
from mitmproxy import http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow:http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
    def response(self,flow):
        # 判断是否是想要的请求信息，通过url判断
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.pretty_url:
            # 修改原始数据
            # 获取的text是str类型，如果对数据进行操作，需要进行数据转换
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "你好，姚苗欣修改名字的值"
            data["data"]["items"][1]["quote"]["name"] = "你好，姚苗欣修改名字的值"
            data["data"]["items"][2]["quote"]["name"] = "你好，姚苗欣修改名字的值"
            flow.response.text = json.dumps(data)

addons = [
    Counter()
]