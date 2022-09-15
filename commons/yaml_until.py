# _*_ coding: utf-8 _*_
# @Time     : 2022/9/14 12:42
# @Author   : Mr_Li
# @FileName : yaml_until.py
import os
import yaml


class YamlUntil:

    # 读
    def read_testcase_yaml(self, yaml_path):
        with open(os.getcwd() + yaml_path, mode='r', encoding='UTF-8') as yml:
            value = yaml.load(stream=yml, Loader=yaml.FullLoader)
            return value

    # 写
    def wtite_yaml(self, data):
        with open(os.getcwd() + "/extract.yaml", mode='a', encoding='UTF-8') as yml:
            yaml.dump(data, stream=yml, allow_unicode=True)

    # 清空
    def clear_yaml(self):
        with open(os.getcwd() + "/extract.yaml", 'w', encoding='UTF-8') as yml:
            yml.truncate()
