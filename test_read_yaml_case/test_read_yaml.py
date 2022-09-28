# _*_ coding: utf-8 _*_
# @Time     : 2022/9/28 12:13
# @Author   : Mr_Li
# @FileName : test_read_yaml.py
from commons.request_page import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


class TestSoftAddaPI:

    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("/test_soft_action_add.yaml"))
    def test_soft_action_add_api(self, test_data):
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        data = test_data["request"]["data"]
        res = HttpRequest().send_all_request(method=method, url=url, json=data)
        print(res.status_code)
        print(res.json())


if __name__ == '__main__':
    pytest.main()
