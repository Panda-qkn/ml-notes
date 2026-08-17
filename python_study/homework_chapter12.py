# -*- coding: utf-8 -*-
"""
第12章 IO编程 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第12章作业已推送，请批改"
本章定位：with + encoding='utf-8' + 逐行读日志 + json 读写配置——脚本从"玩具"变"工具"
注意：日志文件造在 E:\\Study\\ml-notes\\python\\ 目录下（见笔记要求）
"""
import os
import json
import logging


# ========== 必做1：日志解析器（综合实战）（TODO：自己动手写） ==========
# 题目拆解：
#   1. 造一个 50 行 test_run.log（混合 INFO/PASS/FAIL/ERROR 行）
#      格式：[2026-08-09 10:00:01] [FAIL] TC002 login timeout
#      提示：参考第6章作业造 fake_log 的循环写法，写到文件里
#   2. 逐行读取（with + for line in f），统计各级别数量
#      提示：用第6章的生成器思路逐行处理；级别用 line.split 或 in 判断
#   3. 结果写入 JSON 文件 report.json（{"PASS": 20, "FAIL": 8, ...}，indent=2）
#      提示：json.dump(字典, f, indent=2)
#   4. 全程 logging 输出进度，不用 print
LOG_PATH = os.path.join(os.path.dirname(__file__), "test_run.log")

def make_log(path):
    # TODO: 造50行日志写入文件
    pass

def count_levels(path):
    # TODO: 逐行读取统计，返回 {"INFO": x, "PASS": x, "FAIL": x, "ERROR": x}
    pass

def write_report(counts, path):
    # TODO: json.dump
    pass


# ========== 必做2：目录清扫器（TODO：自己动手写） ==========
# 题目拆解：扫描指定目录
#   1. 找出所有 .log 文件，打印文件名和大小（KB）
#      提示：os.listdir / os.path.getsize(path) / 判断 name.endswith('.log')
#   2. 大于 10KB 的 log 文件名收集成列表，存进 big_logs.json
#   （选做可改 pathlib 版：Path(dir).glob('*.log')）
def scan_logs(directory):
    # TODO
    pass


# ========== 选做：StringIO 假文件测试（TODO：自己动手写） ==========
# 题目拆解：把必做1的统计逻辑抽出函数 count_levels(file_obj)
#   用 StringIO 构造假日志做 unittest 单元测试——不落盘就能测文件解析逻辑
#   提示：
#     from io import StringIO
#     fake = StringIO("[2026-08-09 10:00:01] [FAIL] TC002 login timeout\n...")
#     count_levels(fake) 直接传，函数里 for line in file_obj 一样能跑
#   关键：让 count_levels 接收"文件对象"而不是"路径"，真假文件都能喂


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    # --- 必做1 验收 ---
    # make_log(LOG_PATH)
    # counts = count_levels(LOG_PATH)
    # write_report(counts, "report.json")
    # 期望：report.json 内容类似 {"INFO": ..., "PASS": ..., "FAIL": ..., "ERROR": ...}
    #      四种级别数量加起来 = 50

    # --- 必做2 验收 ---
    # scan_logs(os.path.dirname(__file__))
    # 期望：打印各 .log 文件名+大小；big_logs.json 里是 >10KB 的文件名列表

    # --- 选做 验收 ---
    # py -m unittest -v homework_chapter12.py
    pass
