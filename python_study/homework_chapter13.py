# -*- coding: utf-8 -*-
"""
第13章 进程和线程 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第13章作业已推送，请批改"
本章定位：并发网络请求的正确姿势其实是 asyncio/aiohttp（教程第21章），LLM评测平台批量调接口时会用到
Windows 注意：multiprocessing 代码必须放在 if __name__ == '__main__': 保护里
"""
import time
import threading
import random


# ========== 必做1：并发执行用例模拟（TODO：自己动手写） ==========
# 题目拆解：开 5 个线程模拟并发执行用例
#   每个线程 time.sleep(随机1~3秒) 后把结果 append 到共享列表
#   第一版：故意不加锁跑10次，观察有没有异常
#   第二版：加 Lock 修正
#   注释写体会
#   提示：
#     t = threading.Thread(target=worker, args=(...))
#     t.start() 后别忘了 t.join()
#     锁的用法：lock = threading.Lock() → with lock: results.append(...)
results = []
lock = threading.Lock()

def worker(name):
    # TODO: sleep 随机1~3秒，append 结果到共享列表
    pass

def run_no_lock():
    # TODO: 第一版，不加锁，跑10次观察
    pass

def run_with_lock():
    # TODO: 第二版，加锁
    pass


# ========== 必做2：进程池加速（TODO：自己动手写） ==========
# 题目拆解：用 multiprocessing.Pool(4) 的 map 计算 range(1000000) 每个数的平方根之和
#   对比单进程 map(math.sqrt, ...) 的耗时
#   计时：直接用第7章的 @timer 装饰器（from homework_chapter7 import timer）
#   注释回答：为什么小任务量时多进程反而更慢？
#   提示：
#     from multiprocessing import Pool
#     with Pool(4) as p: s = sum(p.map(math.sqrt, range(1000000)))
#     Windows 下必须放 __main__ 保护里！
import math
from multiprocessing import Pool

# TODO: def calc_single(): ...   （单进程版，加 @timer 或手动计时）
# TODO: def calc_pool(): ...     （进程池版）
# 答：为什么小任务量时多进程反而更慢？


# ========== 选做：概念问答（答案写在下面注释里，每题两句话以内） ==========
# 1. GIL 锁住了什么？为什么 IO 密集型线程仍然有用？
# 答：
#
# 2. 多进程在 Windows 为什么必须写 if __name__ == '__main__':？
# 答：
#
# 3. join() 不加会怎样？
# 答：


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # --- 必做1 验收 ---
    # run_no_lock()     # 观察10次有没有异常
    # run_with_lock()   # 加锁版
    # print(results)

    # --- 必做2 验收 ---
    # calc_single()
    # calc_pool()
    # 期望：两版结果一致，耗时打印出来对比
    pass
