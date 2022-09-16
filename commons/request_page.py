# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 17:01
# @Author   : Mr_Li
# @FileName : request_page.py
import requests
import time


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

    def get_random(self):
        return str(int(time.time()))
