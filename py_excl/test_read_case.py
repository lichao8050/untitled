# _*_ coding: utf-8 _*_
# @Time     : 2022/9/16 10:44
# @Author   : Mr_Li
# @FileName : test_read_case.py

from py_excl.read_excel import ExcelReader
from commons.request_page import HttpRequest
import unittest


class TestLoginApi:

    def test_login(self):
        excel = ExcelReader(r"D:\untitled\py_excl\test_excel.xlsx")
        method = excel.get_method(0)
        url = excel.get_url(0)
        data = excel.get_request_data(0)
        headers = excel.get_headers(0)
        print(data)
        res = HttpRequest().send_all_request(method=method, url=url, params=data)
        print(res.json())
        print(res.status_code)



if __name__ == '__main__':
    TestLoginApi().test_login()

# print(excel.get_case_count())
# print(excel.get_test_case_describe(0))
# print(excel.get_method(0))
# print(excel.get_url(0))
# print(excel.get_request_data(0))
