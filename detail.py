# -*- coding: utf-8 -*-
import requests
import json
'''
本函数可获得
商品链接 ， 图片链接 ， 原价 ， 封面图 ，商品标题 ，折后价
 
'''
def detail(id):
    url = "http://tool.chaozhi.hk/api/tb/GetNumiidInfo.php"

    querystring = {"num_iids": id}
    headers = {

    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json = response.json()
    try:
        item_url = json['results']['n_tbk_item']['item_url']
        num_iid = json['results']['n_tbk_item']['num_iid']
        pict_url = json['results']['n_tbk_item']['pict_url']
        reserve_price = json['results']['n_tbk_item']['reserve_price']
        small_images = json['results']['n_tbk_item']['small_images']
        title = json['results']['n_tbk_item']['title']
        zk_final_price = json['results']['n_tbk_item']['zk_final_price']
        return pict_url, title, item_url, num_iid, reserve_price, small_images, zk_final_price
    except:
        return 'id输入错误'

if __name__ == '__main__':
    print (detail('51'))