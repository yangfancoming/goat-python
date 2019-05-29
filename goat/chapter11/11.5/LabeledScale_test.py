# coding: utf-8

from tkinter import *
# 导入ttk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.scale = ttk.LabeledScale(self.master,
            from_ = -100,  # 设置最大值
            to = 100,  # 设置最小值
#            compound = BOTTOM # 设置显示数值的Label在下方
        )
        self.scale.value = -20
        self.scale.pack(fill=X, expand=YES)
root = Tk()
root.title("LabeledScale测试")
App(root)
root.mainloop()
