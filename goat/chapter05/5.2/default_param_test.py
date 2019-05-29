# coding: utf-8

# 为两个参数指定默认值
def say_hi(name = "孙悟空", message = "欢迎来到疯狂软件"):
	print(name, ", 您好")
	print("消息是：", message)
# 全部使用默认参数
say_hi()
# 只有message参数使用默认值
say_hi("白骨精")
# 两个参数都不使用默认值
say_hi("白骨精", "欢迎学习Python")
# 只有name参数使用默认值
say_hi(message = "欢迎学习Python")

say_hi("欢迎学习Python")

#say_hi(name="白骨精", "欢迎学习Python")

#say_hi("欢迎学习Python" , name="白骨精")

say_hi("白骨精", message="欢迎学习Python")
say_hi(name="白骨精", message="欢迎学习Python")
