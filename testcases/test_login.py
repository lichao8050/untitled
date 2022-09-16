# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 11:42
# @Author   : Mr_Li
# @FileName : test_login.py

import requests
from commons.request_page import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


# fixture
@pytest.fixture(scope='session', autouse=True)
def clear_cookie_data():
    YamlUntil().clear_yaml()


class TestApi:

    # 登录接口
    # @pytest.mark.parametrize('test_data', ["haha", "xixi"])
    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("/testcases/test_login.yaml"))
    def test_login_api(self, test_data):
        print(test_data)
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        data = test_data["request"]["data"]
        res = HttpRequest().send_all_request(method=method, url=url, params=data)
        # print(res.json())
        dic = {'cookie': res.headers['Set-Cookie']}
        YamlUntil().write_yaml(dic)
        cookie = res.headers['Set-Cookie']

    # # 软装执行项目新增接口
    # @pytest.mark.parametrize("test_data", YamlUntil().read_testcase_yaml("/testcases/test_soft_action_add.yaml", ))
    # def test_soft_action_add(self, test_data):
    #     method = test_data["request"]["method"]
    #     url = test_data["request"]["url"]
    #     data = test_data["request"]["data"]
    #     res = HttpRequest().send_all_request(method=method, url=url, json=data)
    #     print(res.json())
