# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 10:19
# @Author   : Mr_Li
# @FileName : commons.py

import requests


class HttpRequest:
    sess = requests.session()

    def test_all_request(self, method, url, **kwargs):
        res = HttpRequest.sess.request(method, url, **kwargs)
        return res
