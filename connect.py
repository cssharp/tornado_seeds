# coding:utf-8
# Created by PyCharm.
# Author  : nick（飞虎队工作室）
# Wechat  : cai9503
# Shop    : https://shop.zbj.com/6463852/
# Date    : 2021/10/6
# Time    : 23:09
# connect.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


HOSTNAME = '192.168.2.12'
PORT = '3307'
DATABASE = 'tornado'
USERNAME = 'root'
PASSWORD = 'root'

db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

#1. 引擎
engine = create_engine(db_url)

#2. 连接
connection = engine.connect()
result = connection.execute('select 1')
print(result.fetchone())

#3. 会话
Session = sessionmaker(engine)
session = Session()

#4 基类
Base = declarative_base(engine)
