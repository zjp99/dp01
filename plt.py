# -*- coding: utf-8 -*-#

"""
File         :      plt.py
Description  :  
Author       :      赵金朋
Modify Time  :      2019/5/23 8:39
plt函数的学习
"""
import  matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

#plt.figure()
#plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
#plt.plot(x,y2)
#plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.xlim(-1,5)
plt.ylim(-2,10)

plt.xlabel('x')
plt.ylabel('y')


plt.xticks(np.linspace(-1,2,5))
#plt.yticks([-2,2,6],[r'$ggg$',r'$ooo\ \alpha$','dddd'])

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

l1,=plt.plot(x,y2,label='up')
l2,=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(handles=[l1,l2],labels=['aa','bb'],loc='best')
plt.show()
