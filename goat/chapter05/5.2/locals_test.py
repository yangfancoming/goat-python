# coding: utf-8

def test ():
    age = 20
    # 直接访问age局部变量
    print(age) # 输出20
    # 访问函数局部范围的“变量数组”
    print(locals()) # {'age': 20}
    # 通过函数局部范围的“变量数组”访问age变量
    print(locals()['age']) # 20
    # 通过locals函数局部范围的“变量数组”改变age变量的值
    locals()['age'] = 12
    # 再次访问age变量的值
    print('xxx', age) # 依然输出20
    # 通过globals函数修改x全局变量
    globals()['x'] = 19
x = 5
y = 20
print(globals()) # {..., 'x': 5, 'y': 20}
# 在全局访问内使用locals函数，访问的是全局变量的“变量数组”
print(locals()) # {..., 'x': 5, 'y': 20}
# 直接访问x全局变量
print(x) # 5
# 通过全局变量的“变量数组”访问x全局变量
print(globals()['x']) # 5
# 通过全局变量的“变量数组”对x全局变量赋值
globals()['x'] = 39
print(x) # 输出39
# 在全局范围内使用locals函数对x全局变量赋值
locals()['x'] = 99
print(x) # 输出99
