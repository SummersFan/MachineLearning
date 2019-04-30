from numpy import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

datingDataMat = array([1,2],[2,4],[2,4],[2,4],[2,4],[2,4],[2,4],[2,1])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[0:,1],datingDataMat[0:,2])
plt.show()

x = arange(1,10) #实例2设置X轴
y = x
fig = plt.figure()
ax1 = fig.add_subplot(111)
#设置标题
ax1.set_title('Scatter Plot')
#设置X轴标签
plt.xlabel('X')
#设置Y轴标签
plt.ylabel('Y')
#画散点图
ax1.scatter(x,y,c = 'r',marker = 'o')
#设置图标
plt.legend('x1')
#显示所画的图
plt.show()