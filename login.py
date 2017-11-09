# -*- coding: utf-8 -*-
import requests
import re
'''
注册网站 http://tool.chaozhi.hk
5000次/10元
'''

def login(user_name,passwd):

    url = 'http://tool.chaozhi.hk/api/wx/wx-login.php'

    data = {
        'user_name': user_name,
        'user_pass': passwd,
    }
    headers = {

    }
    response = requests.request("POST", url, data=data, headers=headers)
    _cookie = response.cookies

    all_cookies = ''
    for item in _cookie:
        _name = item.name
        _value = item.value
        all_cookies  =all_cookies+ _name + '=' + _value + ';'
        print (all_cookies)
    #cookies存入本地 data/cookies.txt
    txt = open(r'data/cookies.txt', 'w')
    txt.write(all_cookies)
    txt.close

    return all_cookies
