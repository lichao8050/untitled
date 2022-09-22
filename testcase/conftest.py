# _*_ coding: utf-8 _*_
# @Time     : 2022/9/21 10:08
# @Author   : Mr_Li
# @FileName : conftest.py
import pytest
from commons.request_page import HttpRequest
"""
一、conftest.py的特点
1、可以跨.py文件调用，有多个.py文件调用时，可让conftest.py只调用了一次fixture，或调用多次fixture
2、conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件
3、不需要import导入
conftest.py，pytest用例会自动识别该文件，放到项目的根目录下就可以全局目录调用了，如果放到某个package下，
那就在该package内有效，可有多个conftest.py
4、conftest.py配置脚本名称是固定的，不能改名称
5、conftest.py文件不能被其他文件导入
6、所有同目录测试文件运行前都会执行conftest.py文件
二、conftest.py的使用场景
1、每个接口需共用到的token
2、每个接口需共用到的测试用例数据
3、每个接口需共用到的配置信息
三、conftest.py的生效范围
1、比如下面的示例，我的conftest文件在testcase的目录下，那么testcase这个目录下的所有的城市用例都可以使用conftest文件"""


@pytest.fixture(scope='class', autouse=True)
def test_login():
    print(50 * '*' + '开始测试' + 50 * '*')
    url = r'http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login'
    data = {
        "username": "heqiangming",
        "password": "abc123456"
    }
    method = 'post'
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    res = HttpRequest().send_all_request(method=method, url=url, params=data)

    print("登录获取session：%s" % res.headers['set-Cookie'])
    yield res
