# _*_ coding: utf-8 _*_
# @Time     : 2022/9/28 12:13
# @Author   : Mr_Li
# @FileName : conftest.py
import pytest
from commons.request_page import HttpRequest
from commons.yaml_until import YamlUntil


@pytest.fixture(scope='class', autouse=True)
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
    yield res


