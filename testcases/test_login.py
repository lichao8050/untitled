# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 11:42
# @Author   : Mr_Li
# @FileName : test_login.py

import requests
from commons.request_until import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


class TestApi:

    # 登录接口
    # @pytest.mark.parametrize('test_data', ["haha", "xixi"])
    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("/testcases/test_login.yaml"))
    def test_login_api(self, test_data):
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        headers = test_data["request"]["headers"]
        params = test_data["request"]["data"]
        res = HttpRequest().send_all_request(method=method, url=url, params=data)
        print(res.json())

    # 软装执行项目新增接口
    @pytest.mark.parametrize("test_data", YamlUntil().read_testcase_yaml("/testcases/test_soft_action_add.yaml"))
    def test_soft_action_add(self, test_data):
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        json = test_data["request"]["json"]
        res = HttpRequest().send_all_request(method=method, url=url, json=data)
        print(res.json())
