# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 11:42
# @Author   : Mr_Li
# @FileName : test_login.py

import requests
from commons.request_until import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


class TestApi:

    # def setup(self):
    #     print("每个用例执行之前的操作")
    #
    # def teardown(self):
    #     print("每个用例执行之后的操作")
    #
    # def setup_class(self):
    #     print("每个类执行之前的操作")
    #
    # def teardown_class(self):
    #     print("每个类执行之前的操作")
    # 登录接口
    # @pytest.mark.parametrize('test_data', ["haha", "xixi"])
    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("/testcases/test_login.yaml"))
    def test_login_api(self, test_data):
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        headers = test_data["request"]["headers"]
        data = test_data["request"]["data"]
        res = HttpRequest().send_all_request(method=method, url=url, headers=headers, data=data)
        print(res.json())
        method = consifo["request1"]["method1"]
        url = consifo["request1"]["url1"]
        headers = consifo["request1"]["headers"]
        json = consifo["request1"]["json"]
        res = HttpRequest().send_all_request(method=method, url=url, json=json)
        print(res.json())

    # 软装执行项目新增接口
    @pytest.mark.parametrize("test_data", YamlUntil().read_testcase_yaml("/testcases/test_soft_action_add.yaml"))
    def test_soft_action_add(self, test_data):
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        headers = test_data["request"]["headers"]
        json = test_data["request"]["json"]
        res = HttpRequest().send_all_request(method=method, url=url, json=json)
        print(res.json())
