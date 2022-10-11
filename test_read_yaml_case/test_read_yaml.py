# _*_ coding: utf-8 _*_
# @Time     : 2022/9/28 12:13
# @Author   : Mr_Li
# @FileName : test_read_yaml.py
from commons.request_page import HttpRequest
from commons.yaml_until import YamlUntil
import pytest
import jsonpath


class TestSoftAddaPI:

    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("/test_soft_action_add.yaml"))
    def test_soft_action_add_api(self, test_data):
        print(50 * '*' + '开始执行测试' + 50 * '*')
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        data = test_data["request"]["data"]
        tatil = test_data["title"]
        validate = test_data["request"]["validate"]
        res = HttpRequest().send_all_request(method=method, url=url, json=data)
        print("接口描述：%s" % tatil)
        print("响应代码：%s" % res.status_code)
        print("响应数据：%s" % res.json())
        css = res.json()
        assert css['message'] == validate


if __name__ == '__main__':
    pytest.main(['-vs', '-q'])
