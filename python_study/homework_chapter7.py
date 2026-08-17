# -*- coding: utf-8 -*-
"""
第7章 函数式编程 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第7章作业已推送，请批改"
本章定位：装饰器要会写，其余看得懂即可（看 Allure/pytest 源码会用到）
"""


# ========== 必做1：sorted + lambda（TODO：自己动手写） ==========
# 题目拆解：元组 = (版本号, 通过率%)
#   1. 按通过率降序排列并打印
#      提示：sorted(builds, key=lambda x: ..., reverse=True)
#   2. 按版本号升序排列并打印
#      提示：key 直接取元组第0个元素；字符串排序这里够用
builds = [("V2.1.3", 85), ("V2.1.1", 92), ("V2.2.0", 78), ("V2.1.2", 99)]

# TODO: by_rate = ...
# TODO: by_version = ...


# ========== 必做2：手写装饰器（本章唯一要"会写"的） ==========
# 题目拆解：写装饰器 @timer，打印被装饰函数的执行耗时
#   提示：import time / import functools
#   结构：def timer(func): 内部定义 wrapper(*args, **kw)，
#         前后各 time.time()，打印差值，return func 的返回值
#   必须加 @functools.wraps(func)，然后打印被装饰函数的 __name__ 验证元信息没丢
import time
import functools

def timer(func):
    # TODO: 在这里写装饰器逻辑
    pass

@timer
def slow_task():
    time.sleep(1.5)
    return "任务完成"


# ========== 选做：闭包计数器（TODO：自己动手写） ==========
# 题目拆解：make_counter() 返回一个函数，每调用一次返回递增计数(1,2,3...)
#   要求：用闭包实现，不许用全局变量
#   提示：外层函数里 count = 0，内层函数用 nonlocal count
#   验证：做两个独立计数器，各自计数互不影响（闭包各自持有状态）
def make_counter():
    # TODO: 在这里写闭包逻辑
    pass


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # --- 必做1 验收 ---
    # print(by_rate)
    # 期望：[('V2.1.2', 99), ('V2.1.1', 92), ('V2.1.3', 85), ('V2.2.0', 78)]
    # print(by_version)
    # 期望：[('V2.1.1', 92), ('V2.1.2', 99), ('V2.1.3', 85), ('V2.2.0', 78)]

    # --- 必做2 验收 ---
    # result = slow_task()
    # 期望：打印耗时约 1.5 秒，然后返回 "任务完成"
    # print(slow_task.__name__)
    # 期望：slow_task   （不加 functools.wraps 会变成 wrapper，元信息丢失）

    # --- 选做 验收 ---
    # c1 = make_counter()
    # c2 = make_counter()
    # print(c1(), c1(), c1())   # 期望：1 2 3
    # print(c2())               # 期望：1   （c2 独立计数，不受 c1 影响）
    pass
