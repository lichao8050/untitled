# _*_ coding: utf-8 _*_
# @Time     : 2022/9/16 10:44
# @Author   : Mr_Li
# @FileName : test_read_case.py

from py_excl.read_excel import ExcelReader
from commons.request_page import HttpRequest
import unittest

# 定义读取表格变量excel
excel = ExcelReader(r"D:\untitled\py_excl\test_excel.xlsx")
#  定义统计所有列的变量count_raw
count_row = excel.get_case_count()
for row in range(0, count_row):  # 循环语句   row是变量  范围是0到count
    test_casediscrible = excel.get_test_case_describe(row)
    print(test_casediscrible)
# 模拟读取表格定义的单条数据进行接口请求
# class TestLoginApi:
#
#     def test_login(self):
#         # 定义读取表格变量excel
#         excel = ExcelReader(r"D:\untitled\py_excl\test_excel.xlsx")
#         method = excel.get_method(0)
#         url = excel.get_url(0)
#         data = eval(excel.get_request_data(0))
#         headers = excel.get_headers(0)
#         print(data)
#         res = HttpRequest().send_all_request(method=method, url=url, params=data)
#         print(res.json())
#         print(res.status_code)
#
#
#
# if __name__ == '__main__':
#     TestLoginApi().test_login()

# print(excel.get_case_count())
# print(excel.get_test_case_describe(0))
# print(excel.get_method(0))
# print(excel.get_url(0))
# print(excel.get_request_data(0))
