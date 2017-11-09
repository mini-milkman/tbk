# tbk
taobaoke 转链
各个文件作用
getid.py
  需要在www.taokouling.com 注册账号
  传入参数，淘口令或者淘宝分享短链接
  传出参数，商品id
  
detail.py 
  传入商品id，获取商品信息。
  包括，商品淘宝原链接，商品图片，标题，价格。

gaoyong.py
    需要设置自己的淘宝客的推广渠道位id，和展示位id；并且需要在http://tool.chaozhi.hk 注册自己账号。
    传入参数 商品id，传出参数 申请成功的最大佣金率。
    
gettkl.py
    需要http://tool.chaozhi.hk 的cookie 
    传入参数（淘口令三要素）：商品链接，图片链接，商品标题
    传出参数 转链后的淘口令 
    
