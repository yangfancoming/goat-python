# coding: utf-8

import matplotlib.pyplot as plt


x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
ln1, = plt.plot(x_data, y_data, color = 'red', linewidth = 2.0, linestyle = '--')
ln2, = plt.plot(x_data, y_data2, color = 'blue', linewidth = 3.0, linestyle = '-.')
import matplotlib.font_manager as fm
# 使用Matplotlib的字体管理器加载中文字体
my_font=fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf") 
# 调用legend函数设置图例
#plt.legend(handles=[ln2, ln1], labels=['疯狂Android讲义年销量', '疯狂Java讲义年销量'],
#    loc='lower right', prop=my_font)
plt.legend(labels=['疯狂Java讲义年销量', '疯狂Android讲义年销量'], 
    loc='lower right', prop=my_font)
# 调用show()函数显示图形
plt.show()

