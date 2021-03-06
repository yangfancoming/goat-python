# coding: utf-8

import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 创建pygal.HorizontalLine对象（水平折线图）
horizontal_line = pygal.HorizontalLine()
# 添加两组代表折线的数据
horizontal_line.add('疯狂Java讲义', y_data)
horizontal_line.add('疯狂Android讲义', y_data2)
# 设置Y轴（确实如此）的刻度值
horizontal_line.x_labels = x_data
# 重新设置X轴（确实如此）的刻度值
horizontal_line.y_labels = [20000, 40000, 60000, 80000, 100000]
horizontal_line.title = '疯狂图书的历年销量'
# 设置X、Y轴的标题
horizontal_line.x_title = '销量'
horizontal_line.y_title = '年份'
# 设置将图例放在底部
horizontal_line.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
horizontal_line.render_to_file('fk_books.svg')
