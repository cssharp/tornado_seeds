# coding:utf-8
# Created by PyCharm.
# Author  : nick（飞虎队工作室）
# Wechat  : cai9503
# Shop    : https://shop.zbj.com/6463852/
# Date    : 2021/10/6
# Time    : 20:57
#配置文件
import os

BASE_DIR = os.path.dirname(__file__)

# 变量的配置
options = {
    "port": 8002,
}


settings = {
    "static_path": os.path.join(BASE_DIR, 'static'),
    'template_path': os.path.join(BASE_DIR, 'template'),
    'upfile_path': os.path.join(BASE_DIR, 'upfile'),
    'debug': True,
    "xsrf_cookies" : True,                                  # 开启csrf验证
}