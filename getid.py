# -*- coding: utf-8 -*-
import requests
import re
import json
'''
账号申请网址
http://www.taokouling.com
'''

def dwz(url):
    response = requests.request("GET", url)
    html = response.text

    trurl = re.findall(r"var url = '(.*?)';", html, re.S)
    id = re.findall(r"var url = 'https://a.m.taobao.com/i(.*?).htm?", html, re.S)

    return trurl[0], id[0]

def tkl(koul):

    url = "http://www.taokouling.com/index.php"

    querystring = {"m": "api", "a": "taokoulingjm"}

    data = {
        'username' : '****',#自行设置
        'password' : '*****',#自行设置
        'text' : koul
    }
    response = requests.request("POST", url, data=data, params=querystring).json()
    trurl = response['url']
    title = response['content']
    picurl = response['picUrl']
    try:
        id = re.findall(r"https://a.m.taobao.com/i(.*?).htm?", trurl, re.S)[0]
    except:
        id = re.findall(r'&id=(.*?)&',trurl,re.S)[0]
    return  trurl , title , picurl ,id

def getid(msg):
    if msg[0:4] == 'http':
        return dwz(msg)
    elif msg[0:3] == '￥':
        print tkl(msg)[3]
        return tkl(msg)
    else:
        return '请输入正确的短网址，或淘口令'

if __name__ == '__main__':
    print (getid('￥NUSk0gzbHZk￥'))
