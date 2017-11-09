# -*- coding: utf-8 -*-
import requests
import json
from login import *

# 需要参数 1.商品id 2.商品图片 3.商品文案（标题）4.优惠券链接
def gettkl(msg):
    txt = open(r'data/cookies.txt', 'r')
    cookies = txt.read()
    txt.close
    id = msg[0]
    logo = msg[1]
    text = msg[2]
    gy_url = msg[3]
    #print (msg)

    url = "http://tool.chaozhi.hk/api/tb/GetTkl_free_v3.php"

    payload = {
        'itemId': id,
        'logo': logo,
        'pid': 'mm_119036100_33730388_120100867',
        'shareID': '',  # 分享者淘宝数字ID
        'text': text,
        'url': gy_url
    }
    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'origin': "http://tool.chaozhi.hk",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'dnt': "1",
        'referer': "http://tool.chaozhi.hk/wxlink-v3/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8",
        'cookie': cookies
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    json = response.json()
    #print (json)
    model = json['data']['model']
    tbk_spread = json['results']['tbk_spread'][0]['content']
    err_msg = json['results']['tbk_spread'][0]['err_msg']
    return model, tbk_spread, err_msg

