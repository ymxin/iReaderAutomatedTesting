#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/6 8:46 上午
# @Author : miaoxinyao
# @Email : murcymurcy@163.com
# @File : test_contact.py
# @Project : iReaderAutomatedTesting

import requests


def get_token():
    '''
    获取token
    :return:
    '''
    get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8a97a9d7d2f57334&corpsecret=9_Rkq0A6b8wjLoJ_VZTRn4x6FWYANF2uORK-qH8fcX0'
    r = requests.get(get_token_url)
    token = r.json()['access_token']
    return token

def test_find_member():
    '''
    获取成员信息
    :return:
    '''
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=YaoMiaoXin'
    r = requests.get(get_member_url)
    print(r.json())
    assert '姚苗欣' == r.json()['name']

def test_update_member():
    '''
    更新成员信息
    :return:
    '''
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data = {
        'userid': 'aa_007',
        'name':'aa_007李四',
        'mobile':'18333601212'
    }
    r = requests.post(url=update_member_url,json=data)
    print(r.json())

def test_delete_member():
    '''
    删除成员信息
    :return:
    '''
    delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=aa_007'
    r = requests.get(delete_member_url)
    print(r.json())

def test_create_member():
    '''
    创建成员信息
    :return:
    '''
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "aa_007",
        "name": "aa_007",
        "alias": "小妖怪",
        "mobile": "+86 18333604725",
        "department": [4],
    }
    r = requests.post(url=create_member_url,json=data)
    print(r.json())



