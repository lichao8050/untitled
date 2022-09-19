# _*_ coding: utf-8 _*_
# @Time     : 2022/9/19 9:38
# @Author   : Mr_Li
# @FileName : test_add_soft_action.py
from commons.request_page import HttpRequest
import pytest
from commons.yaml_until import YamlUntil


@pytest.fixture(scope='session', autouse=True)
def test_login_api():
    method = "post"
    url = r'http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login'
    data = {
        'username': 'heqiangming',
        'password': 'abc123456'
    }
    res = HttpRequest().send_all_request(method=method, url=url, params=data)
    print(res.headers['set-cookie'])
    print(res.json())


class TestSoftAddaPI:

    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("/testcases/test_soft_action_add.yaml"))
    def test_soft_action_add_api(self, test_data):
        method = test_data["request"]["method"]
        url = test_data["request"]["url"]
        data = test_data["request"]["data"]
        res = HttpRequest().send_all_request(method=method, url=url, json=data)
        print(res.status_code)
        print(res.json())
