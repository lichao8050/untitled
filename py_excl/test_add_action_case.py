# _*_ coding: utf-8 _*_
# @Time     : 2022/9/16 10:44
# @Author   : Mr_Li
# @FileName : test_add_action_case.py

from py_excl.read_excel import ExcelReader
from commons.request_page import HttpRequest
import unittest
import pytest


# 定义读取表格变量excel
excel = ExcelReader(r"D:\untitled\py_excl\test_excel.xlsx")
#  定义统计所有列的变量count_raw
count_row = excel.get_case_count()
for row in range(0, count_row):  # 循环语句   row是变量  范围是0到count
    test_casediscrible = excel.get_test_case_describe(row)
    url = excel.get_url(row)
    data = eval(excel.get_request_data(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
    method = excel.get_method(row)
    headers = eval(excel.get_headers(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
    res = HttpRequest().send_all_request(method=method, headers=headers, url=url, params=data)
    print(res.json())
    print(res.status_code)
excel = ExcelReader(r"D:\untitled\py_excl\test_selectaction_excel.xlsx")
#  定义统计所有列的变量count_raw
count_row = excel.get_case_count()
for row in range(0, count_row):  # 循环语句   row是变量  范围是0到count
    url2 = excel.get_url(row)
    data2 = eval(excel.get_request_data(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
    method2 = excel.get_method(row)
    res1 = HttpRequest().send_all_request(method=method2, url=url2, params=data2)
    print(res1.json())
    print(res1.status_code)

