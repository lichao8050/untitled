# _*_ coding: utf-8 _*_
# @Time     : 2022/9/14 12:42
# @Author   : Mr_Li
# @FileName : yaml_until.py
import os
import yaml


class YamlUntil:

    # 读
    def read_testcase_yaml(self, yaml_file):
        with open(yaml_file, 'r', encoding='UTF-8') as yml:
            value = yaml.load(stream=yml, Loader=yaml.FullLoader)
            return value

    # 写
    def wtite_yaml(self, data):
        with open(os.getcwd() + "/extract.yaml", 'r', encoding='UTF-8') as yml:
            value = yaml.load(stream=yml, Loader=yaml.FullLoader)

    # 清空
    def clear_yaml(self, key):
        with open(os.getcwd() + "/extract.yaml", 'r', encoding='UTF-8') as yml:
            value = yaml.load(stream=yml, Loader=yaml.FullLoader)
            return value[key]
