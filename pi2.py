#!/usr/bin/python

import math

a=0.0
b=0.0
t=0.0
p=0.0
a_ant=1.0
b_ant=1.0/math.sqrt(2.0)
t_ant=(1.0/4)
p_ant=1.0
x=0.0

while(x<100):

   a=(a_ant+b_ant)/2
   b=math.sqrt(a_ant*b_ant)
   t = t_ant - (p_ant*(pow((a_ant-a),2)))
   p=2*p_ant

   numpi=(math.pow((a + b),2)/(4*t))

   a_ant=a
   b_ant=b
   t_ant=t
   p_ant=p
   x+=1


print('%2.40f'%numpi)
