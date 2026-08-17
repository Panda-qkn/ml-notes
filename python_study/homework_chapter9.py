# -*- coding: utf-8 -*-
"""
第9章 面向对象编程 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第9章作业已推送，请批改"
本章定位：继承+多态是测试框架的骨架模式；getattr/hasattr 反射三件套是理解插件机制的钥匙
"""


# ========== 必做1：测试用例类体系（TODO：自己动手写） ==========
# 题目拆解：
#   基类 TestCase：
#     __init__(self, case_id, title)
#     run()    打印 "执行 {case_id}"
#     result() 返回 "UNKNOWN"
#   子类 FuncTestCase：
#     重写 result() 返回 "PASS"
#     重写 run()：先打印 "[功能测试]"，再调用 super().run()
#   子类 PerfTestCase：
#     重写 result() 返回 "BLOCK"（模拟性能用例排队）
#   提示：__init__ 里别忘了 super().__init__(case_id, title)
class TestCase:
    # TODO
    pass

class FuncTestCase(TestCase):
    # TODO
    pass

class PerfTestCase(TestCase):
    # TODO
    pass


# ========== 必做2：类属性计数器（TODO：自己动手写） ==========
# 题目拆解：
#   1. 给 TestCase 加类属性 total = 0，__init__ 里 TestCase.total += 1
#      提示：注意写的是 TestCase.total 不是 self.total，想清楚为什么
#   2. 实例化5个用例后打印 TestCase.total
#   3. 故意给某个实例 s.total = 999，再打印 TestCase.total 和 s.total
#      注释解释两者为何不同（提示：实例属性遮蔽类属性）


# ========== 选做：反射小工具（TODO：自己动手写） ==========
# 题目拆解：inspect_obj(obj) 打印 obj 所有【不含下划线开头】的属性名，
#   并标注每个是不是方法
#   提示：dir(obj) 拿全部名字；过滤用 not name.startswith('_')；
#         getattr(obj, name) 拿属性；callable(...) 判断是不是方法
def inspect_obj(obj):
    # TODO
    pass


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # --- 必做1 验收 ---
    # cases = [
    #     FuncTestCase("TC001", "登录测试"),
    #     FuncTestCase("TC002", "注册测试"),
    #     PerfTestCase("TC003", "并发压测"),
    #     PerfTestCase("TC004", "大数据量查询"),
    # ]
    # for case in cases:
    #     case.run()
    #     print(f"{case.result()}")
    # 期望：循环代码不需要 if 判断类型，但功能用例打印 "[功能测试] 执行 TCxxx"，
    #       result 各自正确 —— 这就是多态

    # --- 必做2 验收 ---
    # （实例化5个用例后）
    # print(TestCase.total)   # 期望：5
    # s.total = 999
    # print(TestCase.total, s.total)   # 期望：5 999，注释解释原因

    # --- 选做 验收 ---
    # inspect_obj(FuncTestCase("TC009", "反射测试"))
    # 期望：打印 case_id、title、result、run 等，方法后面标注 "(方法)"
    pass
