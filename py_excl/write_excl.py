# _*_ coding: utf-8 _*_
# @Time     : 2022/4/25 20:24
# @Author   : Mr_Li
# @FileName :

from openpyxl import Workbook

# Python创建一个Excel表格
book = Workbook()
sheet = book.active
sheet['A1'] = 11
sheet['A2'] = 23

book.save("test_excel.xlsx")
