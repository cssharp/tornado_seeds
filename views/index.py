# coding:utf-8
# Created by PyCharm.
# Author  : nick（飞虎队工作室）
# Wechat  : cai9503
# Shop    : https://shop.zbj.com/6463852/
# Date    : 2021/10/6
# Time    : 20:58
import tornado.web
from tornado.httpclient import AsyncHTTPClient
import json
import os
from config import settings
from tornado import gen
from connect import session
from models.User import User


# 视图层
class IndexHandler(tornado.web.RequestHandler):
    # 接受get请求
    def get(self):
        print('get。。。。')
        # self.write('hello world。。')   # 相当于Django框架中的HttpResponse
        self.render('index.html')

    # 接受post请求
    def post(self):
        pass


class DetailHandler(tornado.web.RequestHandler):
    def get(self, id, *args, **kwargs):
        print(id)          # 接受无名传参
        self.write(id)     # 响应回去


class DictinfoHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request)
        info = {
            "name": 'lxxx',
            "age": 18
        }
        infoStr = json.dumps(info)  # 序列化
        self.write(infoStr)  # 返回json数据

    def post(self, *args, **kwargs):
        name = self.get_argument('name', strip=True)       # 获取单个值
        pwd = self.get_argument('pwd', strip=True)       # 获取单个值
        hobby = self.get_arguments('hobby', strip=True)
        # self.get_arguments(name, strip)    # 获取复选框传过来的值

        info = {
            'name': name,
            'pwd': pwd,
            'hobby': hobby
        }
        self.set_header('nick', 'cai') # 设置响应头header头信息  (*****)
        self.set_status(200, '收到了')  # 设置响应的状态码以及状态的原因
        self.write(info)


class WenjianHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('uploadfile.html')  # 返回上传页面
        # self.set_status(999)               # 设置响应状态码

    def post(self, *args, **kwargs):
        filesDict = self.request.files  # 接收文件数据
        print(filesDict)  # 打印接收到文件数据

        # 下载文件
        for key, val in filesDict.items():
            for filesinfo in val:
                filename = filesinfo['filename']
                uppath = os.path.join(settings['upfile_path'], filename)
                with open(uppath, 'wb') as fp:
                    fp.write(filesinfo['body'])


class StudentHandler(tornado.web.RequestHandler):
    # 请求函数
    @gen.coroutine  # 协程方式获取异步处理结果
    def get(self, *args, **kwargs):
        print('协程方式获取异步处理结果')
        url = "http://www.baidu.com/"
        client = AsyncHTTPClient()  # 异步客户端
        res = yield client.fetch(url)  # 发起异步请求,执行回调函数

        if res.error:  # 执行错误情况下
            self.send_error(500)
        else:  # 执行正确的情况下
            ret = res.body
            self.write(ret)
        self.finish()  # 执行完关闭连接


class UserHandler(tornado.web.RequestHandler):
    def get(self, id, *args, **kwargs):
        userobj = session.query(User).filter(User.id==id).first()
        print(userobj)
        print(id)          # 接受有名传参
        if userobj:
            self.write(userobj.username)     # 响应回去
        else:
            self.write('没有找到')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', strip=True)       # 获取单个值
        password = self.get_argument('password', strip=True)       # 获取单个值
        person = User(username=username, password=password)
        session.add(person)
        session.commit()
        self.write("创建成功")
        self.set_status(301, '创建成功')  # 设置响应的状态码以及状态的原因
        self.redirect('/')

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            self.write('error:' + str(status_code))


