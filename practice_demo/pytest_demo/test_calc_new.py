# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # @Time : 2021/7/2 8:42 上午
# # @Author : miaoxinyao
# # @Email : murcymurcy@163.com
# # @File : test_calc_new.py
# # @Project : iReaderAutomatedTesting
#
# import pytest
# import yaml
#
# from practice_demo.python_code.calc import Calculator
#
# with open('./datas/calc.yaml') as f:
#     datas = yaml.safe_load(f)['add']
#     add_datas = datas['datas']
#     print(add_datas)
#     myids = datas['myids']
#     print(myids)
#
#
# class TestCalc:
#     def setup(self):
#         print("开始计算")
#         # 实例化计算机类
#         self.calc = Calculator()
#
#     def teardown(self):
#         print("结束计算")
#
#     @pytest.mark.parametrize(
#         "a,b,expect", add_datas, ids=myids
#     )
#     def test_add(self, a, b, expect):
#         result = self.calc.add(a, b)
#         # 判断结果是否正确
#         if isinstance(result, float):
#             assert round(result, 2) == expect
#
#     @pytest.mark.add
#     def test_add2(self):
#         # # 实例化计算机类
#         # calc = Calculator()
#         # 判断结果是否正确
#         assert self.calc.add(0.1, 2) == 2.1
#
#     def test_add4(self):
#         assert round(self.calc.add(0.1, 0.2), 2) == 0.3
#
#     @pytest.mark.sub
#     def test_sub(self):
#         print("这是一个减法计算")
