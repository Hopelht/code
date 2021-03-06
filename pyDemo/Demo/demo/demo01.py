# import pandas as pd
# import numpy as np
# from nltk.corpus import brown
# brown.words()

# --------------------------------------------------------------
"""网络爬取一张图片"""
# import requests
# #调用requestsku
# path="C:/Users/27761/Desktop/favorite.jpg"
# #确定路径，当然也可以是gif,jpg等格式
# url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1564330508239&di=0805ff4e43126e284164ea505e91e004&imgtype=0&src=http%3A%2F%2Fdingyue.ws.126.net%2F2019%2F04%2F10%2F8c1a3bedd7f94f4c82a07e8e08687c55.jpeg"
# #输入你想要爬取的图片的地址，我喜欢孟美岐，哈哈，所以我就爬取了她的一张图片
# r = requests.get(url)
# #调用get函数进行网页的登录
# r.status_code
# #查看登录是否正常
# with open(path,'wb') as f:
# 	f.write(r.content)
# 	#用二进制写入图片信息
#
# f.close()
#关闭文件写入
# ---------------------------------------------------------------------
def outer(age):
    def inner(name):
        print(name, age)    #内部函数用到了外部的age
    return inner   #是outer的return
demo = outer("17")
demo("zhangsan")
