# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 10:19
# @Author   : Mr_Li
# @FileName : commons.py

import requests
from commons.request_page import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


class TestRequest:
    print(50 * '-' + "开始测试" + 50 * '-')

    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("/testcases/test_login.yaml"))
    def setup(self, test_data):
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        headers = test_data["request"]["headers"]
        data = test_data["request"]["data"]
        res = HttpRequest().send_all_request(method=method, url=url, headers=headers, data=data)
        print(res.json())
        print("每个用例执行之前的操作")

    def teardown(self):
        self.session.close()
        try:
            del self.session.cookies['JSESSIONID']
        except:
            pass
        print("每个用例执行之后的操作")

    # def setup_class(self):
    #     print("每个类执行之前的操作")
    #
    # def teardown_class(self):
    #     print("每个类执行之前的操作")
