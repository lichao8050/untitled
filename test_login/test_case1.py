# _*_ coding: utf-8 _*_
# @Time     : 2022/9/26 12:48
# @Author   : Mr_Li
# @FileName : test_case1.py
import pytest

# 用户注册的夹具@pytest.fixturedef register_user():
# print('---用户注册的夹具前置执行----')
# ...注册代码省略，注册的用户信息如下
# user_info = {'user': 'lemonban', 'pwd': '123456'}
# yield user_info
# print('---用户注册的夹具后置执行----')
# 用户登录的夹具,通过定义形参来使用register_user这个夹具
# @pytest.fixturedef user_login(register_user):
# print('---用户登录的夹具前置执行----')
# 获取register_user结局前置脚本执行完，yeild传递出来的数据
# user_info = register_user
# ...登录代码省略，下面为登录得到的token
# token = 'sdjasjdask'
# yield token
# print('---用户登录的夹具后置执行----')
# 函数用例 指定使用测试夹具
# user_logindef test_func__01(user_login):
# token = user_login
# print("测试用例夹具user_login传递过来的token:",token)
# print("测试用例---test_func__01---")


@pytest.fixture(autouse=True)
def my_fixture():
    print('------my_fixture---前置执行脚本--------')
    yield
    print('------my_fixture---后置执行脚本--------')


class TestDome:

    # 函数用例 指定测试夹具
    def test_02(self):
        print('----测试用例：test_01------')
    # 函数用例 指定测试夹具

    def test_03(self):
        print('----测试用例：test_02------')


class TestDome2:
    # 函数用例 指定测试夹具
    def test_03(self):
        print('----测试用例：test_03------')
