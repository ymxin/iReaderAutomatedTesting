#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/29 8:49 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_address.py
# @Project : iReaderAutomatedTesting
from practice_demo.test_requests_ymx.wework.address import Address


class TestAddress:

    def setup(self):
        self.address = Address()
        self.user_id = 'aa_009'
        self.name = 'aa_009'
        self.mobile = '+86 17600234601'
        self.department = [4]

    def test_create_member(self):
        # 利用删除接口进行数据清理
        self.address.delete_member(self.user_id)
        r = self.address.create_member(self.user_id,self.name,self.mobile,self.department)
        # r['errmsg'] 由于网络不好或其他原因造成不对，就会报错
        # assert r['errmsg'] == 'created'
        # 使用get可以解决这个问题
        assert r.get('errmsg','网络错误或其他原因') == 'created'