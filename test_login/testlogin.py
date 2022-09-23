# _*_ coding: utf-8 _*_
# @Time     : 2022/9/22 18:01
# @Author   : Mr_Li
# @FileName : testlogin.py
from commons.request_page import HttpRequest
from commons.read_excel_until import ExcelReader
import pytest


class TestLogin:

    def test_login(self):
        excel = ExcelReader(r"D:\untitled\excel\login_excel.xlsx")
        count_row = excel.get_case_count()
        for row in range(0, count_row):
            case_describe = excel.get_test_case_describe(row)
            print("用例描述：%s" % case_describe)
            method = excel.get_method(row)
            print("接口请求方法：%s" % method)
            url = excel.get_url(row)
            print("接口请求地址：%s" % url)
            headers = eval(excel.get_headers(row))
            print("接口请求头部：%s" % headers)
            data = eval(excel.get_request_data(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
            print("接口请求数据：%s" % data)
            res = HttpRequest().send_all_request(method=method, headers=headers, url=url, params=data)
            print("接口响应代码：%s" % res.status_code)
            print("接口响应数据：%s" % res.json())
            if res.status_code != int(excel.get_start_code(row)):
                excel.set_pass_or_fail(row, "fail")
            else:
                excel.set_pass_or_fail(row, "pass")
            excel.save_file("D:\\untitled\\excel\\login_excel.xlsx")
            excel.close_file()

            print(res.json().get('name'))
            print(200 * '*')
