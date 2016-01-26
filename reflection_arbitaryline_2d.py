# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:53:40 2016

@author: Sai Guruprasad
"""
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
import numpy.linalg as lg

m=eval(raw_input('Enter the slope of the line : '));
c=eval(raw_input('Enter the intercept of the line : '));
n=eval(raw_input('Enter the number of points to be reflected : '));
A=np.ones([n+1,3]);
for i in range(n):
    A[i,0]=eval(raw_input('Enter the x-coordinate of the point : '));
    A[i,1]=eval(raw_input('Enter the y-coordinate of the point : '));
maxx=np.max(A[:,0]); maxy=np.max(A[:,1]);
x=np.linspace(-(maxx+5),(maxx+5),200);
y=m*x+c;
plt.figure()
plt.plot(x,y);
xl=plt.xlim([-(maxx+5),(maxx+5)]);
yl=plt.ylim([-(maxy+5),(maxy+5)]);
plt.hold('on')
#plt.Line2D([0,0],xl);
theta=-cm.atan(m);
Tr=np.matrix([[1,0,0],[0,1,0],[0,-c,1]]);
Ro=np.matrix([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),0],[0,0,1]]);
Re=np.matrix([[1.0,0,0],[0,-1.0,0],[0,0,1.0]]);
Roi=lg.inv(Ro);
Tri=lg.inv(Tr);
T=Tr*Ro*Re*Roi*Tri;
A_n=A*T;
A[n,0]=A[0,0]; A[n,1]=A[0,1];
A_n[n,0]=A_n[0,0]; A_n[n,1]=A_n[0,1];
plt.hold('on')
plt.plot(A[:,0],A[:,1]);
plt.hold('on')
plt.plot(A_n[:,0],A_n[:,1]);
plt.hold('on')
x=np.linspace(0,0,100);
y=np.linspace(-(maxy+5),(maxy+5),100);
plt.plot(x,y)
plt.hold('on')
x=np.linspace(-(maxx+5),(maxx+5),100);
y=np.linspace(0,0,100);
plt.plot(x,y)
plt.show()