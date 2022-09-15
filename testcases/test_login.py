# _*_ coding: utf-8 _*_
# @Time     : 2022/9/15 11:42
# @Author   : Mr_Li
# @FileName : test_login.py

import requests
from commons.request_until import HttpRequest
from commons.yaml_until import YamlUntil
import pytest


class TestApi:

    @pytest.mark.parametrize('test_data', YamlUntil().read_testcase_yaml("D:\\untitled\\testcases\\test_action_view"
                                                                         ".yaml"))
    def test_action_view(self, test_data):
        print(test_data)
