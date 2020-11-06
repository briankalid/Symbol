#!/usr/bin/env python

from sympy import *

x = Symbol('x')

formule = 'x^3 + 1.0'

y = sympify(formule)
velocity = y.diff(x)
acceleration = velocity.diff(x)

print(y)
print(velocity)

f=lambdify(x,y,'numpy')
f1 = lambdify(x,velocity,'numpy')
f2 = lambdify(x,acceleration,'numpy')

x0=1.5

y0=f(x0)
y1=f1(x0)
y2=f2(x0)

print(y0)
print(y1)
print(y2)
