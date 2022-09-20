# _*_ coding: utf-8 _*_
# @Time     : 2022/9/16 10:44
# @Author   : Mr_Li
# @FileName : test_read_case.py

from py_excl.read_excel import ExcelReader
from commons.request_page import HttpRequest
import unittest
import pytest


@pytest.fixture(scope='session', autouse=True)
def set_start():
    # 定义读取表格变量excel
    excel = ExcelReader(r"D:\untitled\py_excl\login_excel.xlsx")
    #  定义统计所有列的变量count_raw
    count_row = excel.get_case_count()
    for row in range(0, count_row):  # 循环语句   row是变量  范围是0到count
        test_casediscrible = excel.get_test_case_describe(row)
        url = excel.get_url(row)
        data = eval(excel.get_request_data(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
        method = excel.get_method(row)
        headers = eval(excel.get_headers(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
        try:
            res = HttpRequest().send_all_request(method=method, headers=headers, url=url, params=data)
            print(res.json())
            print(res.status_code)
            if res.status_code != int(excel.get_start_code(row)):
                print('这是不同', res.status_code)
                print(int(excel.get_start_code(row)))
                excel.set_pass_or_fail(row, 'fail')
                print(excel.get_is_true_or_fail(row))
            else:
                print('这是相同', res.status_code)
                print(int(excel.get_start_code(row)))
                excel.set_pass_or_fail(row, 'pass')
            excel.save_file()
            excel.close_file()
        except Exception as errors:
            print(errors)
        else:
            pass
