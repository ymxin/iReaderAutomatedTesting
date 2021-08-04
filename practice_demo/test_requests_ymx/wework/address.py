#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/29 8:45 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : address.py
# @Project : iReaderAutomatedTesting
import requests


class Address:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        '''
        获取token
        :return:
        '''
        get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8a97a9d7d2f57334&corpsecret=9_Rkq0A6b8wjLoJ_VZTRn4x6FWYANF2uORK-qH8fcX0'
        r = requests.get(get_token_url)
        token = r.json()['access_token']
        return token

    def find_member(self):
        '''
        获取成员信息
        :return:
        '''
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=YaoMiaoXin'
        r = requests.get(get_member_url)
        print(r.json())
        assert '姚苗欣' == r.json()['name']

    def update_member(self):
        '''
        更新成员信息
        :return:
        '''
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            'userid': 'aa_007',
            'name': 'aa_007李四',
            'mobile': '18333601212'
        }
        r = requests.post(url=update_member_url, json=data)
        print(r.json())

    def delete_member(self, userid):
        '''
        删除成员信息
        :return:
        '''
        delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        # access_token={self.get_token()}&userid={userid}
        # requests特性，可以将URL里的参数，写在params里
        params = {
            'access_token': self.token,
            'userid': userid
        }
        r = requests.get(delete_member_url,params=params)
        return r.json()

    def create_member(self,user_id,name,mobile,department):
        '''
        创建成员信息
        :return:
        '''
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(url=create_member_url, json=data)
        return r.json()
