# coding=utf-8
# 导入Pie组件，用于生成饼图
from pyecharts.charts import Pie

# 获取评论中所有评分
rates = []
with open('蚁人.txt', 'r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        try:
            rate = row.split(',')
        except IndexError:
            continue
        if rate != "":
            rates.append(rate[4])

# # 定义星级
# attr = ['五星', '四星', '三星', '二星', '一星', '零星']
# # 统计各星级评分数量
# v1 = [rates.count('50'), rates.count('40'), rates.count('30'), rates.count('20'), rates.count('10'),
#       rates.count('0')]
data = [['五星', rates.count('50')], ['四星', rates.count('40')], ['三星', rates.count('30')], ['二星', rates.count('20')],
        ['一星', rates.count('10')], ['零星', rates.count('0')]]

pie = Pie()
pie.add("1", data, radius=[40, 75], center=[300, 150], is_clockwise=False)

pie.render('tupi.html')
