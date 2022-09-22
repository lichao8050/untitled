# _*_ coding: utf-8 _*_
# @Time     : 2022/9/16 10:44
# @Author   : Mr_Li
# @FileName : test_add_action_case.py
import pytest
from commons.read_excel_until import ExcelReader
from commons.request_page import HttpRequest


class TestApi:

    @pytest.mark.smoke
    def test_select_action(self):
        """查看执行项目详情"""
        excel = ExcelReader(r"D:\untitled\excel\test_selectaction_excel.xlsx")
        #  定义统计所有列的变量count_raw
        count_row = excel.get_case_count()
        for row in range(0, count_row):  # 循环语句   row是变量  范围是0到count
            case_describe = excel.get_test_case_describe(row)
            print("用例描述：%s" % case_describe)
            method = excel.get_method(row)
            print("接口请求方法：%s" % method)
            url = excel.get_url(row)
            print("接口请求地址：%s" % url)
            data = eval(excel.get_request_data(row))  # 此处参数类型不是字符串，所以用eval转换为字典类型
            print("接口请求数据：%s" % data)
            res = HttpRequest().send_all_request(method=method, url=url, params=data)
            print("接口响应代码：%s" % res.status_code)
            print("接口响应数据：%s" % res.json())
            print(200 * '*')

    @pytest.mark.cttest
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


"""[pytest]
# 配置参数 用例分组
addopts = -vs no:warnings
# 配置测试用例文件夹  测试用例在py_excel文件夹下
testpaths = ./py_excel
# 配置测试用例模块的规则,以test开头可以自定义修改
python_files = test_*.py
# 配置测试用例类的规则
python_classes = Test*
# 配置测试用例方法的规则
python_functions = test_*
# 配置接口测试的基础路径
base_url = http://192.168.20.102:180/
# 给用例分组,自定义  用例上加上@pytest.mark.somking装饰器
markers=
    smoke:冒烟测试
    usermanage:用户登录"""