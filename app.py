# coding:utf-8
# Created by PyCharm.
# Author  : nick（飞虎队工作室）
# Wechat  : cai9503
# Shop    : https://shop.zbj.com/6463852/
# Date    : 2021/10/6
# Time    : 20:57
#项目启动文件
import tornado.ioloop    # tornado框架强大引擎，IO高效核心模块
from urls import App
import config

if __name__ == '__main__':
    app = App()
    app.listen(config.options["port"])        # 绑定端口
    print('端口:[ %s ] 服务已经启动...' % (config.options["port"]))
    tornado.ioloop.IOLoop.current().start()   # 开始监听端口

