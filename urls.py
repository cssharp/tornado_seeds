# coding:utf-8
# Created by PyCharm.
# Author  : nick（飞虎队工作室）
# Wechat  : cai9503
# Shop    : https://shop.zbj.com/6463852/
# Date    : 2021/10/6
# Time    : 20:57
#路由文件
from tornado.web import Application
from views.index import IndexHandler, DetailHandler, DictinfoHandler, WenjianHandler, StudentHandler, UserHandler
from config import settings


# 配置路由
class App(Application):
    def __init__(self):
        url = [
            (r'/', IndexHandler),  # 路由匹配试图函数
            (r'/index/', IndexHandler),  # 路由匹配试图函数
            (r'/no/([0-9]+)/', DetailHandler),  # 路由无名分组
            (r'/detail/(?P<id>[0-9]+)/', DetailHandler),  #  路由有名分组
            (r'/dictinfo/', DictinfoHandler),
            (r'/wenjian/', WenjianHandler),
            (r'/stu/', StudentHandler),
            (r'/user/', UserHandler),
            (r'/user/(?P<id>[0-9]+)', UserHandler),
        ]

        super(App, self).__init__(url, **settings)

