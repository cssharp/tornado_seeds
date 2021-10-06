# coding:utf-8
# Created by PyCharm.
# Author  : nick（飞虎队工作室）
# Wechat  : cai9503
# Shop    : https://shop.zbj.com/6463852/
# Date    : 2021/10/6
# Time    : 23:14
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from connect import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime, default=datetime.now)


if __name__ == "__main__":
    Base.metadata.create_all()
