# coding: utf-8

ac1 = 3 + 0.2j
print(ac1)
print(type(ac1)) # 输出 complex类型
ac2 = 4 - 0.1j
print(ac2)
# 复数运行
print(ac1 + ac2) # 输出 (7+0.1j)
# 导入cmatch模块
import cmath
# sqrt()是cmath模块下的函数，用于计算平方根
ac3 = cmath.sqrt(-1)
print(ac3) # 输出 1j