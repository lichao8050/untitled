# _*_ coding: utf-8 _*_
# @Time     : 2022/9/26 16:15
# @Author   : Mr_Li
# @FileName : conftest.py
import pytest
from commons.request_page import HttpRequest
from commons.read_excel_until import ExcelReader


# 使用pytest夹具定义前置、后置
@pytest.fixture(scope='class', autouse=True)
def get_session():
    print(50 * '*' + '开始测试' + 50 * '*')
    excel = ExcelReader(r"D:\untitled\excel\test_add_new_action.xlsx")
    url = r'http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login'
    data = {
        "username": "heqiangming",
        "password": "abc123456"
    }
    method = 'post'
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    res = HttpRequest().send_all_request(method=method, url=url, params=data)
    print("登录获取session：%s" % res.headers['set-Cookie'])
    yield res, excel
    print(50 * '*' + '结束测试' + 50 * '*')
    excel.close_file()
