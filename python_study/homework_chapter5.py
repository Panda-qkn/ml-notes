# -*- coding: utf-8 -*-
"""
第5章 函数 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第5章作业已推送，请批改"
"""


# ========== 必做1：参数全能函数（示例，Claude 已给出参考答案） ==========
# 题目拆解：
#   build_profile(name, *, level=1, **tags)
#   - name     : 必填位置参数，调用时直接写在最前面
#   - *,       : 星号是分隔线，它后面的参数必须按名字传（这就是"命名关键字参数"）
#   - level=1  : 命名关键字参数，默认1；想改就写 level=6
#   - **tags   : 收集剩下所有"键=值"，在函数内部它是一个 dict
def build_profile(name, *, level=1, **tags):
    # f-string 拼出 "[Lv6] 阿米娅" 这部分
    parts = [f"[Lv{level}] {name}"]
    # tags 是 dict，逐个取出键值对，格式化成 "键=值"
    for k, v in tags.items():
        parts.append(f"{k}={v}")
    # 用 " | " 把所有部分连起来
    return " | ".join(parts)


# ========== 必做2：多返回值解包（TODO：自己动手写） ==========
# 提示：return 总数, 通过率   （逗号隔开就是返回一个 tuple）
def analyze_results(passes, fails, blocks):
    return ((passes+fails+blocks),passes/(passes+fails+blocks)*100)

# ========== 必做3：递归阶乘（TODO：自己动手写） ==========
# 提示：终止条件是 n == 1 时返回 1；否则返回 n * fact(n - 1)
def fact(n):
    print(f"进入 fact({n})")    #每层打印n
    if n==1:
        return 1
    return n * fact(n - 1)
# n=1000 会报错，python递归上限是1000，次数过多会导致栈溢出,打印报错：RecursionError: maximum recursion depth exceeded

# ========== 选做：默认参数陷阱复现（TODO：自己动手写） ==========
def add_case(case, case_list=[]):
    case_list.append(case)
    return case_list

#修改后
def add_caserepair(caserepair,caserepair_list=None):
    if caserepair_list is None:
        caserepair_list = []
    caserepair_list.append(caserepair)
    return caserepair_list

# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # --- 必做1 验收 ---
    result1 = build_profile("阿米娅", level=6, class_="术师", hp=1000)
    print(result1)
    # 期望输出：[Lv6] 阿米娅 | class_=术师 | hp=1000
    # 也试试不传 level：build_profile("博士", job="指挥") 应输出 "[Lv1] 博士 | job=指挥"

    # --- 必做2 验收 ---
    total, pass_rate = analyze_results(80, 15, 5)
    print(f"总数：{total},通过率: {pass_rate:.1f}%")
    
    # --- 必做3 验收 ---
    print(fact(100))

    # --- 选做 验收 ---
    print(add_case("直到大地变成一颗酸橙"))
    print(add_case("你好Doctor"))
    print(add_case("我的粥ID是熊熊的猫"))
    #复现打印如下
    #['直到大地变成一颗酸橙']
    #['直到大地变成一颗酸橙', '你好Doctor']
    #['直到大地变成一颗酸橙', '你好Doctor', '我的粥ID是熊熊的猫']
    
    #问题原因，case_list=[]在def执行时只创建一次，之后每次调用共享的是同一个list对象，所以第一次append的内容在第二次时还存在
    print(add_caserepair("直到大地变成一颗酸橙"))
    print(add_caserepair("你好Doctor"))
    print(add_caserepair("我的粥ID是熊熊的猫"))
    #修改后打印如下
    #['直到大地变成一颗酸橙']
    #['你好Doctor']
    #['我的粥ID是熊熊的猫']