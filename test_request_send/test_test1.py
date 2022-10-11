# _*_ coding: utf-8 _*_
# @Time     : 2022/10/11 10:20
# @Author   : Mr_Li
# @FileName : test_test1.py

import requests

a = range(0, 10)
for i in a:
    if i <= 10:
        url = r'http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login'
        data = {
            "username": "zhongqiuhong",
            "password": "abc123456"
        }
        res = requests.post(url=url, data=data)
        print(res.json())
        print(res.headers['set-Cookie'])
        cookie_1 = res.headers['set-Cookie']
        cookie_2 = cookie_1[22:78]
        print(cookie_2)

        url2 = r'http://kbs.matrixdesign.cn/api/authapi/wf_ProcessInst/getMyTaskPagedList'
        data_1 = {
            "skipCount": 1,
            "maxResultCount": 10,
            "sorting": "startDate descending",
            "key": "3",
            "businessId": "BX202200730"
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "%s" % cookie_2
        }
        res2 = requests.post(url=url2, json=data_1, headers=headers)
        print(res2.json())
        print(i)
        i += 1
