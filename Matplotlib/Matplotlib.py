import matplotlib.pyplot as plt
import numpy as np

#生成一组数据50个
x = np.linspace(-3, 3, 50)

#构建二元一次方程
y1 = 2*x + 1
y2 = x ** 2

#第一个窗口，大小（8，5）
plt.figure(num = 1,figsize = (8,5))
#将值展示出来
plt.plot(x,y1)

#第二个窗口，大小默认值
plt.figure(num = 2)
#将值展示出来，同一张图显示两条线，第二条红色、虚线
plt.plot(x,y2)
plt.plot(x,y1,color = 'red', linestyle = '--')
#设置x，y显示的范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#为x,y加标签
plt.xlabel('i am x')
plt.ylabel('i am y')
#自定义y坐标轴
plt.yticks([-2,-1.8,-1,1.22,2,3], [r'$iii$','a','m','q','b','l'])
#gca = 'get current axis'
ax = plt.gca()
#将右、上坐标轴隐藏
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#定义哪条线为x，哪条为y
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#调整坐标轴的位置
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))


#在脚步中需要用show将图像展示出来，将两个窗口都显示出来
plt.show()