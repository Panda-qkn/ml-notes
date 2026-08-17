# -*- coding: utf-8 -*-
"""
第14章 正则表达式 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第14章作业已推送，请批改"
口诀：raw 字符串写模式、search/findall 最常用、括号分组做提取、默认贪婪加问号
调试工具：regex101.com 在线调试，比脑算快十倍
"""
import re


# ========== 必做1：日志行结构化提取（TODO：自己动手写） ==========
# 题目拆解：对第12章作业的日志格式 [2026-08-09 10:00:01] [FAIL] TC002 login timeout
#   1. 写正则提取 日期、时间、级别、用例ID、消息 五个分组
#      提示：r'\[(...)\] \[(...)\] (...) (...)'，五个括号五组
#   2. 用预编译 pattern 处理全部50行，输出结构化列表（每行一个 dict）
#      提示：pattern = re.compile(...)；m = pattern.match(line)；m.groups()
#   3. 附加：用 findall 从整个日志中直接提取所有 FAIL 用例的 ID 列表
LOG_LINE = "[2026-08-09 10:00:01] [FAIL] TC002 login timeout"

# TODO: pattern = re.compile(r'...')
def parse_log_line(line):
    # TODO: 返回 {"date": ..., "time": ..., "level": ..., "case_id": ..., "msg": ...}
    pass

def extract_fail_ids(log_text):
    # TODO: findall 一把提取所有 FAIL 用例 ID
    pass


# ========== 必做2：协议人专属（送分题）（TODO：自己动手写） ==========
# 题目拆解：写三个校验函数，各自返回 True/False
#   提示：re.fullmatch 做整串校验最顺手
#   每个函数配 3 正 2 反的测试数据跑一遍（用第11章 unittest 更佳）
def is_ipv4(s):
    # TODO: 校验合法 IPv4，注意 0-255 边界，"999.1.1.1" 要 False
    # 提示：单段 0-255 的正则可以写 (25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)
    pass

def is_mac(s):
    # TODO: 校验 AA:BB:CC:DD:EE:FF 格式
    pass

def is_version(s):
    # TODO: 校验 V主.次.修订 格式，如 V2.1.3
    pass


# ========== 选做：贪婪实验（TODO：自己动手写） ==========
# 题目拆解：对 "a<div>111</div>b<div>222</div>c"
#   分别用 <div>.+</div> 和 <div>.+?</div> 做 findall
#   打印结果并在注释里解释差异
#   提示：默认贪婪——能多吃就多吃；? 变非贪婪——少吃一口是一口
s = "a<div>111</div>b<div>222</div>c"
# TODO: greedy = re.findall(r'<div>.+</div>', s)
# TODO: lazy = re.findall(r'<div>.+?</div>', s)
# 差异解释：


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # --- 必做1 验收 ---
    # print(parse_log_line(LOG_LINE))
    # 期望：{'date': '2026-08-09', 'time': '10:00:01', 'level': 'FAIL',
    #       'case_id': 'TC002', 'msg': 'login timeout'}
    # （50行全量验证：读第12章的 test_run.log 逐行 parse）
    # print(extract_fail_ids(open('test_run.log', encoding='utf-8').read()))
    # 期望：所有 FAIL 用例 ID 的列表

    # --- 必做2 验收 ---
    # ipv4 正例：192.168.1.1 / 0.0.0.0 / 255.255.255.255
    # ipv4 反例：999.1.1.1 / 192.168.1
    # mac  正例：AA:BB:CC:DD:EE:FF / 00:11:22:33:44:55 / aa:bb:cc:dd:ee:ff
    # mac  反例：AA-BB-CC-DD-EE-FF / AA:BB:CC:DD:EE
    # ver  正例：V2.1.3 / V0.0.1 / V10.20.30
    # ver  反例：2.1.3 / V2.1

    # --- 选做 验收 ---
    # print(greedy)   # 期望：['<div>111</div>b<div>222</div>']（一口吞）
    # print(lazy)     # 期望：['<div>111</div>', '<div>222</div>']
    pass
