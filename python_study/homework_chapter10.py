# -*- coding: utf-8 -*-
"""
第10章 面向对象高级编程 · 课后作业
交作业流程：写代码 → 本地运行通过 → 双击 push.bat 推送 → 告诉Claude"第10章作业已推送，请批改"
本章定位：@property 用在配置/状态类上；枚举用在用例状态上；__str__ 和 __getitem__ 最实用
"""


# ========== 必做1：@property 校验版配置类（TODO：自己动手写） ==========
# 题目拆解：TestEnv 类
#   _url 私有存储；url 用 @property 暴露
#   setter 里校验：必须以 http:// 或 https:// 开头，否则 raise ValueError
#   再加一个只读 property is_https 返回布尔
#   提示：
#     @property            def url(self): return self._url
#     @url.setter          def url(self, value): 校验后 self._url = value
#     只读 = 只写 @property 不写 setter
class TestEnv:
    # TODO
    pass


# ========== 必做2：枚举 + __str__（TODO：自己动手写） ==========
# 题目拆解：
#   1. 定义 Result 枚举（PASS / FAIL / BLOCK）
#      提示：from enum import Enum; class Result(Enum): PASS = 1 ...
#      （也可以试试 auto()）
#   2. 把第9章作业1的 TestCase 搬过来，result() 返回枚举成员
#   3. 给 TestCase 加 __str__，返回 "[TC001] 登录测试 -> PASS" 格式
#      提示：__str__ 里 return 一个 f-string；枚举成员名用 .name 拿
from enum import Enum

# TODO: class Result(Enum): ...
# TODO: class TestCase: ...（带 __str__）


# ========== 选做：__getitem__ 伪装列表（TODO：自己动手写） ==========
# 题目拆解：TestSuite 类实现 __len__ 和 __getitem__
#   让它支持 len(suite)、suite[0]、for case in suite、切片 suite[:2]
#   提示：内部用一个 self._cases 列表存；__getitem__(self, i) 直接 return self._cases[i]
#         （切片传进来的 i 是 slice 对象，list 天然支持，不用特判）
#   体会"鸭子类型"：不用继承 list 就能像 list
class TestSuite:
    # TODO
    pass


# ========== 调用测试区：运行这个文件看输出 ==========
if __name__ == "__main__":
    # --- 必做1 验收 ---
    # env = TestEnv()
    # env.url = "https://test.example.com"   # 合法，正常赋值
    # print(env.url, env.is_https)           # 期望：https://test.example.com True
    # try:
    #     env.url = "ftp://bad"              # 非法，应抛 ValueError
    # except ValueError as e:
    #     print("校验生效:", e)

    # --- 必做2 验收 ---
    # case = FuncTestCase("TC001", "登录测试")
    # print(case)   # 期望：[TC001] 登录测试 -> PASS（print 自动调 __str__）

    # --- 选做 验收 ---
    # suite = TestSuite()
    # （往里装4个用例）
    # print(len(suite))       # 期望：4
    # print(suite[0])         # 期望：第1个用例
    # for c in suite[:2]:     # 期望：前2个用例
    #     print(c)
    pass
