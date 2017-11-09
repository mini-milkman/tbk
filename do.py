# -*- coding: utf-8 -*-
import requests
import json
from detail import *
from gaoyong import *
from getid import *
from gettkl import *
'''
生成淘口令
短链接
错误代码

'''
#获取三要素 图片 标题 链接
def _info(msg):
    #读取本地cookies
    txt = open(r'data/cookies.txt', 'r')
    cookies = txt.read()
    txt.close
    #获取id  www.taokouling.com  无需cookies
    try:
        id1 = getid(msg)[3]
        str.isdigit(str(id1)) == 'True'
        id = id1
        print id
    except:
        #print (getid(msg))
        return 'id获取失败'
    #获取商品详情
    try :
        logo = detail(id)[0]
        text = detail(id)[1]
        print (logo , text)
    except:
        return '未找到商品信息'
    #申请高佣
    try :
         url = gysq(id)
         print (url)
    except:
        return '无高佣信息'
    #print (id ,text ,url)
    return id ,logo ,text ,url

#三要素转为淘口令
def _gettkl(msg):
    try:
        _allinfo = _info(msg)
        return gettkl(_allinfo)
    except:
        return '淘口令转化失败'


if __name__ == '__main__':
    msg = raw_input(r'请输入淘口令或宝贝链接：')
    mimade = _gettkl(msg)
    print mimade[0],mimade[1],mimade[2]