# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:12:14 2020

@author: Kohei Yoshida
"""
import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bc(a,f,k):
    a[k,:] = 0
    a[:,k] = 0
    a[k,k] = 1
    f[k] = 0
    return(a,f)

def visualize(u_visualize,t):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xx = np.arange(N_x)
    yy = np.arange(N_y)
    X,Y = np.meshgrid(xx,yy)
    ax.plot_surface(X, Y, u_visualize, cmap='plasma', linewidth=0, vmax=0.7)
    ax.set_zlim(0, 1.5)
    plt.savefig('v1_%d.png' % t,format = 'png' ,dpi = 200, transparent = True)
    plt.show()
    
#離散化条件を定義
N_x = 50
N_y = 50

x = 1
y = 1

dx = x/N_x
dy = y/N_y
dt = 0.05

alpha = 0.01
vx = 1
vy = 1

time_step = 100

#A行列を定義
a = np.zeros((N_x*N_y,N_x*N_y))
for i in range(N_x*N_y):
    a[i,i] = 1 + (vx/dx + vy/dy + 2*alpha/dx**2 + 2*alpha/dy**2)*dt
    
    if i-N_x>=0:
        a[i,i-N_x] = -(vy/dy + alpha/dy**2)*dt
    if i-1>=0:
        a[i,i-1] = -(vx/dx + alpha/dx**2)*dt
    if i+1<N_x*N_y:
        a[i,i+1] = -alpha*dt/dx**2
    if i+N_x<N_x*N_y:
        a[i,i+N_x] = -alpha*dt/dy**2

u = np.zeros((N_x*N_y,time_step))
f = np.zeros(N_x*N_y)

#初期条件（ステップ波）
i = 0
j = 0
for i in range(4,20):
    for j in range(4,20):
        k = N_x*j+i
        u[k,0] = 1


#境界条件
i = 0
for j in range(N_y):
    k = N_x*j + 0
    a,f = bc(a,f,k)
    
    k = N_x*j + N_x-1
    a,f = bc(a,f,k)
    
j = 0
for i in range(N_x):
    k = N_x*0 + i
    a,f = bc(a,f,k)
    
    k = N_x*(N_y-1) + i
    a,f = bc(a,f,k)

#初期条件の可視化
u_list = []
u_visualize = u[:,0].reshape(N_y,N_x)
t = 0
visualize(u_visualize, t)


#行列演算による解析および可視化
for t in range(1,time_step):
    f_bar = u[:,t-1] + f*dt
    u[:,t] = scipy.linalg.solve(a,f_bar)
    u_visualize = u[:,t].reshape(N_y,N_x)
    u_list.append(u_visualize)
    visualize(u_visualize, t)
    