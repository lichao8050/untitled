# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 17:01
# @Author   : Mr_Li
# @FileName : request_page.py
import requests
import time


class HttpRequest:
    session = requests.session()

    def send_all_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        res = ""
        if method == 'get':
            res = HttpRequest.sess.request(method, url, params=data, **kwargs)
        elif method == 'post':
            res = HttpRequest.sess.request(method, url, json=data, **kwargs)
        return res

    def get_random(self):
        return str(int(time.time()))
