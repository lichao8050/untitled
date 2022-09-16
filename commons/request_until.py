# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 10:19
# @Author   : Mr_Li
# @FileName : commons.py

import requests
from commons.request_page import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


# class TestRequest:
#     print(50 * '-' + "开始测试" + 50 * '-')
#
#     def setup(self):
#         print("每个用例执行之前的操作")
#
#     def teardown(self):
#         self.session.close()
#         try:
#             del self.session.cookies['JSESSIONID']
#         except:
#             pass
#         print("每个用例执行之后的操作")

    # def setup_class(self):
    #     print("每个类执行之前的操作")
    #
    # def teardown_class(self):
    #     print("每个类执行之前的操作")
