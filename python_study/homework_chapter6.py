# -*- coding: utf-8 -*-
"""
第6章 高级特性 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第6章作业已推送，请批改"
"""


# ========== 必做1：切片三连（TODO：自己动手写） ==========
# 题目拆解：不用循环，只用切片  L[开始:结束:步长]（左闭右开）
#   1. 从 'OSPFISISBGPRIPMPLS' 取出 'BGP'
#      提示：先数清楚 B 和 P 的下标，注意"结束"是右开的
#   2. 把 [1,2,3,4,5,6,7,8,9,10] 逆序
#      提示：步长可以是负数
#   3. 取出偶数位元素（下标1,3,5...的值）
#      提示：从哪个下标开始？步长是多少？
def slice_practice():
    protocols = 'OSPFISISBGPRIPMPLS'
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice_practice1 = protocols[8:11]
    slice_practice2 = numbers[::-1]
    slice_practice3 = numbers[1:11:2]
    
    return (
        slice_practice1,
        slice_practice2,
        slice_practice3,
        )
    


# ========== 必做2：列表生成式实战（TODO：自己动手写） ==========
# 题目拆解：
#   results 是 (用例ID, 结果) 的 tuple 列表
#   - 一行取出所有 FAIL 用例 ID -> ['TC002', 'TC004']
#     提示：[x for x in results if ...]，x 是 tuple，可以用解包 for tc, r in results
#   - 一行转成 ['TC001:PASS', 'TC002:FAIL', ...]
#     提示：f'{tc}:{r}'
results = [("TC001", "PASS"), ("TC002", "FAIL"), ("TC003", "PASS"), ("TC004", "FAIL"), ("TC005", "BLOCK")]
#failed_ids = [x[0] for x in results if x[1] == "FAIL"]
#学习使用解包和f-string，已在obsidian上追加笔记
failed_ids = [case_id for case_id, status in results if status == "FAIL"]
formatted = [f"{case_id}:{status}" for case_id, status in results]


# ========== 必做3：生成器读"大日志"（TODO：自己动手写） ==========
# 题目拆解：
#   写生成器 read_failed(lines)，逐行检查，含 "FAILED" 的行才 yield
#   提示：for line in lines: if "FAILED" in line: yield ...
#   然后造20行假日志（其中5行含 FAILED），for 循环消费并打印行号+内容
#   提示：带下标用 enumerate
def read_failed(lines):
    # TODO: 在这里写生成器逻辑  这题不会做，完全没有理解生成器
    # 作业参考答案
    for line in lines:
        if "FAILED" in line:
            yield line

def count_to(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1

# 补交作业
def read_by_result(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

# ========== 选做：递归 vs 生成器思考（TODO：自己动手写） ==========
# 题目拆解：用 yield 输出斐波那契前20项
# 提示：参考笔记 6.4 的 fib(max) 模板
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a +b
        n = n + 1
    return 'done' 
# TODO（注释里回答）：为什么递归不适合改成生成器？
# （提示：生成器是"拉"模型，递归是"压栈"）
# 答：递归函数可以直接拿到最终的结果，而生成器需要遍历，类似阶乘、斐波那契数列这种只需要一个最终结果的场景
# 用生成器反而别扭，因为生成器设计出来是为了逐个产生一系列值
# 计算型递归（需要子结果做运算）改生成器确实两头不占；但遍历型递归（逐个产出元素）改生成器是黄金搭档，内存和提前终止都是巨大优势


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # --- 必做1 验收 ---
    # 期望输出：
    # BGP
    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # [2, 4, 6, 8, 10]
    slice_practice()
    print(*slice_practice(),sep='\n')
    # 实际输出：
    #BGP
    #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #[2, 4, 6, 8, 10]

    # --- 必做2 验收 ---
    # print(failed_ids)   # 期望：['TC002', 'TC004']
    # print(formatted)    # 期望：['TC001:PASS', 'TC002:FAIL', 'TC003:PASS', 'TC004:FAIL', 'TC005:BLOCK']
    print(failed_ids) 
    print(formatted)
    #实际输出结果：
    #['TC002', 'TC004']
    #['TC001:PASS', 'TC002:FAIL', 'TC003:PASS', 'TC004:FAIL', 'TC005:BLOCK']

    # --- 必做3 验收 ---
    fake_log = []
    for i in range(1, 21):
        if i % 4 == 0:  # 第4,8,12,16,20行含 FAILED，共5行
            fake_log.append(f"TC{i:03d} result=FAILED")
        else:
            fake_log.append(f"TC{i:03d} result=PASSED")
    # for 行号, 内容 in enumerate(read_failed(fake_log), 1):
    #     print(f"第{行号}行: {内容}")
    print(fake_log)
    for 行号,内容 in enumerate(read_failed(fake_log), 1):
        print(f"第{行号}行：{内容}")
    print(list(read_failed(fake_log)))
    #补交作业 把 `read_failed` 复制进作业文件跑通后，再加一个 `read_by_result(lines, keyword)`：
    # 筛选词变成参数，分别用它打印 FAILED 行和 PASSED 行。
    for 行号,内容 in enumerate(read_by_result(fake_log,"FAILED"), 1):
        print(f"第{行号}行：{内容}")
    for 行号,内容 in enumerate(read_by_result(fake_log,"PASSED"), 1):
        print(f"第{行号}行：{内容}")
    print(list(read_by_result(fake_log,"FAILED")))
    print(list(read_by_result(fake_log,"PASSED")))
    
    g = count_to(3)
    print(next(g))
    print(next(g))
    print(next(g))
    
    # --- 选做 验收 ---
    for n in fib(20):
        print(n, end=" ")
    # 期望输出：1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
