# -*- coding: utf-8 -*-
"""
第8章 模块 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第8章作业已推送，请批改"
本章定位：__main__ 判断 + venv + pip 国内源，每个自动化项目的"开门三件事"
注意：本章必做1需要拆成多个文件，按提示在 python_study 目录下新建
"""


# ========== 必做1：双形态模块（TODO：新建文件） ==========
# 题目拆解：
#   1. 新建 netstat_tool.py，含函数 summary(results)：
#      接收 [("PASS", 3), ("FAIL", 1)] 形式的列表，返回汇总字典 {"PASS": 3, "FAIL": 1}
#      文件底部加 if __name__ == '__main__': 直接运行时打印一个演示
#   2. 新建 main.py，import netstat_tool 并调用 summary
#      验证：import 时【不触发】netstat_tool 里的演示打印
#
# 参考骨架（把下面的代码分别放进两个文件）：
#
# --- netstat_tool.py ---
# def summary(results):
#     # TODO: 遍历 results，累加到字典
#     # 提示：d[k] = d.get(k, 0) + v
#     pass
#
# if __name__ == '__main__':
#     # 直接运行本文件时才执行的演示代码
#     print(summary([("PASS", 3), ("FAIL", 1)]))
#
# --- main.py ---
# import netstat_tool
# print(netstat_tool.summary([("PASS", 10), ("FAIL", 2), ("BLOCK", 1)]))
# 观察：运行 main.py 时，netstat_tool 的演示打印【不应该】出现


# ========== 必做2：建你的第一个 venv（命令行任务，不写代码） ==========
# 题目拆解：在 E:\Study\ml-notes\ 下操作（Windows 终端）
#   py -m venv .venv                          # 创建虚拟环境
#   .venv\Scripts\activate                    # 激活（Git Bash 用 source .venv/Scripts/activate）
#   py -m pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple   # 清华源安装
#   py -c "import requests; print(requests.__version__)"   # 验证
#   py -m pip freeze > requirements.txt       # 导出依赖清单，提交到仓库
# 验收：把 requests 版本号告诉 Claude；requirements.txt 已提交
# 注意：以后每装新包都重新执行 pip freeze 更新 requirements.txt


# ========== 选做：包结构（TODO：改造必做1） ==========
# 题目拆解：把必做1改造成包
#   python_study/
#     nettools/
#       __init__.py      # 里面写：from .stats import summary
#       stats.py         # 把 summary 函数挪进来
#     main.py            # 改成：from nettools import summary
# 体会：模块是单个 .py 文件，包是带 __init__.py 的文件夹


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # 本章作业主体在其他文件/命令行，这里留一个快速自测：
    # 把你的 summary 实现临时贴在这里验证也行
    # demo = [("PASS", 3), ("FAIL", 1)]
    # 期望：{'PASS': 3, 'FAIL': 1}
    pass
