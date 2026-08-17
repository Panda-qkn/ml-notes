# -*- coding: utf-8 -*-
"""
第11章 错误调试和测试 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第11章作业已推送，请批改"
本章定位：setUp/tearDown ≈ 测试环境准备/恢复，assertRaises ≈ 异常用例，logging ≈ 测试日志规范
注意：unittest 用命令行跑：py -m unittest -v homework_chapter11.py
"""


# ========== 必做1：给第5章作业写单元测试（TODO：自己动手写） ==========
# 题目拆解：用 unittest 给 build_profile 写测试类，至少5个用例
#   正常：仅必填参数 / 带 level / 带多个 tags
#   异常：level 传字符串时（先给函数加上类型检查并 raise TypeError，再用 assertRaises 验证）
#   边界：tags 为空
#   要求：用 setUp 准备公共数据，跑 py -m unittest -v 全绿
#   提示：
#     import unittest
#     from homework_chapter5 import build_profile  # 同目录直接 import
#     注意：build_profile 原始版没有类型检查，先在这里定义加强版再测
import unittest

# TODO: 先定义加强版 build_profile（加 isinstance 检查，level 非 int 时 raise TypeError）

# TODO: class TestBuildProfile(unittest.TestCase):
#           def setUp(self): ...
#           def test_仅必填参数(self): ...   用 assertEqual
#           def test_带level(self): ...
#           def test_带多个tags(self): ...
#           def test_tags为空(self): ...
#           def test_level传字符串(self): ...
#               with self.assertRaises(TypeError): ...


# ========== 必做2：logging 改造（TODO：自己动手写） ==========
# 题目拆解：
#   1. 把必做1脚本里的 print 全部换成 logging（INFO 级别）
#      提示：logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
#   2. 加一条 logging.exception 演示：在 except 里记录后再 raise
#   3. 观察 logging 和 print 输出的差别：级别、格式、能否关闭
import logging

# TODO


# ========== 选做：doctest 顺手加（TODO：自己动手写） ==========
# 题目拆解：把第6章作业2的列表生成式封装成函数，写 doctest 文档字符串
#   跑 py -m doctest -v homework_chapter11.py 验证
#   提示：docstring 里 >>> 开头是调用，下一行是期望输出
def failed_case_ids(results):
    """取出所有 FAIL 用例 ID

    >>> failed_case_ids([("TC001", "PASS"), ("TC002", "FAIL")])
    ['TC002']
    """
    # TODO: 把第6章的一行列表生成式搬进来
    pass


# ========== 调用测试区 ==========
# 注意：本章 unittest 用命令行跑：py -m unittest -v homework_chapter11.py
# 直接运行本文件时走这里：
if __name__ == "__main__":
    # unittest.main(verbosity=2)   # 也可以这样跑（二选一）
    # import doctest; doctest.testmod(verbose=True)   # 选做验收
    pass
