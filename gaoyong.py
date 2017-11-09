# -*- coding: utf-8 -*-
import requests
import json
from login import *
'''
本函数获得 
高佣申请后的推广链接

'''


def gysq_post(id):
    txt = open(r'data/cookies.txt', 'r')
    cookies = txt.read()
    txt.close
    url = "http://tool.chaozhi.hk/api/tb/ulandPrivilege.php"

    payload = {
        'adzone_id': '120100867',
        'id': id,#淘宝商品id  item_id
        'key': '700021003284d0f3981bbb083d0ca8606ce5af0f161ae2b67efae04c3ee599389cc77e31822358317',
        'site_id': '33730388'
    }

    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'origin': "http://tool.chaozhi.hk",
        'x-devtools-emulate-network-conditions-client-id': "46c553e6-1116-4d2f-9a06-56abc5d1af85",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'dnt': "1",
        'referer': "http://tool.chaozhi.hk/wxlink-v3/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8",
        'cookie': cookies
    }
    #print (headers)
    response = requests.request("POST", url, data=payload, headers=headers)
    return response

def gysq_json(response):
    try:
        json = response.json()
        coupon_click_url = json['result']['data']['coupon_click_url']
        item_id = json['result']['data']['item_id']
        max_commission_rate = json['result']['data']['max_commission_rate']#最高佣金率
        return coupon_click_url
    except:
        login()
        response = gysq_post(id2)
        json = response.json()
        coupon_click_url = json['result']['data']['coupon_click_url']
        item_id = json['result']['data']['item_id']
        max_commission_rate = json['result']['data']['max_commission_rate']  # 最高佣金率
        return coupon_click_url

def gysq(id):
    global id2
    id2 = id
    return gysq_json(gysq_post(id))


if __name__ == '__main__':
    print (gysq_json(gysq_post('535423477888'))) #测试商品id：535423477888
