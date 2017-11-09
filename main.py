# -*- coding: utf-8 -*-
import requests
import json
import re
_verify = ''#cookie 全局变量
id = ''
'''
1.获取商品信息（链接，商品id，图片，标题，价格）  无需cookie
2.申请高佣（获取优惠券链接，最高推广利率,商品id）          需要cookie
3.淘口令，短链接，图片，二合一转链                需要cookie
'''
def getid():
    global id
    id = input('请输入商品id：')
    return id

#登陆获取cookie
def login(user_name,passwd):
    url = 'http://tool.chaozhi.hk/api/wx/wx-login.php'

    data = {
        'user_name': user_name,
        'user_pass': passwd
    }
    headers = {

    }
    #response =  requests.request("POST", url, data=data, headers=headers)
    #_cookie = response.cookies
    #cookie = '<RequestsCookieJar[<Cookie PHPSESSID=aiinn0acjq2c5ctmghfhe5bcs0 for tool.chaozhi.hk/>]>'
    global _verify
    #_verify = re.compile(r'<Cookie (.*?) for tool.chaozhi.hk', re.I).findall(str(_cookie))[0]
    _verify = 'PHPSESSID=4b5usr6pvj24qkok15h7bluak1' #PHPSESSID=qrpbvepc1i9hgr1elklt4fjg25
    print (_verify)
    return _verify

#获取商品详细信息
def detail(id):
    url = "http://tool.chaozhi.hk/api/tb/GetNumiidInfo.php"

    querystring = {"num_iids": id}
    headers = {

    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json = response.json()
    item_url = json['results']['n_tbk_item']['item_url']
    num_iid = json['results']['n_tbk_item']['num_iid']
    pict_url = json['results']['n_tbk_item']['pict_url']
    reserve_price = json['results']['n_tbk_item']['reserve_price']
    small_images = json['results']['n_tbk_item']['small_images']
    title = json['results']['n_tbk_item']['title']
    zk_final_price = json['results']['n_tbk_item']['zk_final_price']
    #print (item_url)
    return pict_url , title

#申请高佣 获取优惠券链接  需要cookie
def gysq(id):
    url = "http://tool.chaozhi.hk/api/tb/ulandPrivilege.php"

    payload = {
        'adzone_id': '', # 自己设置淘宝联盟能看到
        'id': id,#淘宝商品id  item_id
        'key': '700021003284d0f3981bbb083d0ca8606ce5af0f161ae2b67efae04c3ee599389cc77e31822358317',
        'site_id': ''#你的推广位id
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
        'cookie': _verify
    }
    #print (headers)
    response = requests.request("POST", url, data=payload, headers=headers)
    json = response.json()
    coupon_click_url = json['result']['data']['coupon_click_url']
    item_id = json['result']['data']['item_id']
    max_commission_rate = json['result']['data']['max_commission_rate']#最高佣金率

    #print(response.text)
    return coupon_click_url

#图片，链接，文案转淘口令  需要cookie
def gettkl(id):
    url = "http://tool.chaozhi.hk/api/tb/GetTkl_free_v3.php"

    #需要参数 1.商品id 2.商品图片 3.商品文案（标题）4.优惠券链接
    payload = {
        'itemId': id,
        'logo': detail(id)[0],
        'pid': '', #设置成自己的推广pid
        'shareID': '',      #分享者淘宝数字ID
        'text': detail(id)[1],
        'url': gysq(id)
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
        'cookie': _verify
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    json = response.json()
    model = json['data']['model']
    tbk_spread = json['results']['tbk_spread'][0]['content']
    err_msg = json['results']['tbk_spread'][0]['err_msg']
    print (model , tbk_spread , err_msg)
    return model , tbk_spread , err_msg

#二合一链接  需要cookie 只需要高佣返回的链接
def coupon_2in1():
    url = "http://tool.chaozhi.hk/api/tb/GetTkl_free_v3.php"

    payload = {
        'url': gysq(id)
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
        'cookie': _verify
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    json = response.json



if __name__ == '__main__':
    login(user_name,passwd)
    gettkl(getid())