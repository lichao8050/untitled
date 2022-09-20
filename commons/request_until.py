# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 10:19
# @Author   : Mr_Li
# @FileName : commons.py
from py_excl.read_excel import ExcelReader
import requests
from commons.request_page import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


@pytest.fixture(scope='session', autouse=True)
def start1_test():
    rq = HttpRequest()
    url = r'http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login'
    data = {
        "username": "heqiangming",
        "password": "abc123456"
    }
    method = 'post'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    res = rq.send_all_request(method=method, headers=headers, url=url, params=data)
