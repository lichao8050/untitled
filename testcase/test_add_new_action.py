# _*_ coding: utf-8 _*_
# @Time     : 2022/9/22 16:47
# @Author   : Mr_Li
# @FileName : test_add_new_action.py
from commons.read_excel_until import ExcelReader
from commons.request_page import HttpRequest


class TestAddNewAction:

    def test_add_new_action(self):
        excel = ExcelReader(r"D:\untitled\excel\test_add_new_action.xlsx")
        count_row = excel.get_case_count()
        for row in range(0, count_row):
            case_describe = excel.get_test_case_describe(row)
            print("用例描述：%s" % case_describe)
            method = excel.get_method(row)
            print("接口请求方法：%s" % method)
            url = excel.get_url(row)
            print("接口请求地址：%s" % url)
            data = eval(excel.get_request_data(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
            print("接口请求数据：%s" % data)
            res = HttpRequest().send_all_request(method=method, url=url, json=data)
            print("接口响应代码：%s" % res.status_code)
            print("接口响应数据：%s" % res.json())
            print(200 * '*')
