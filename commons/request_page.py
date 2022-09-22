# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 17:01
# @Author   : Mr_Li
# @FileName : request_page.py
import requests
import time
import json
import jsonpath


class HttpRequest:

    session = requests.session()

    def send_all_request(self, method, url, **kwargs):
        method = str(method).lower()
        res = ""
        if method == 'get':
            res = HttpRequest.session.request(method, url, **kwargs)
        elif method == 'post':
            res = HttpRequest.session.request(method, url, **kwargs)
        return res

    #  基于jsonpath获取数据的关键字：用于提取所需要的内容
    def get_text(self, data, key):
        """jsonpath获取数据的表达式：成功则返回list，失败则返回false
         loads是将json格式的内容转换为字典的格式
         jsonpath接收的是dict类型的数据"""
        dict_data = json.loads(data)
        value = jsonpath.jsonpath(dict_data, '$..{0}'.format(key))
        return value[0]

    def get_random(self):
        return str(int(time.time()))
