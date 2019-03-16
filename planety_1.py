# !/usr/bin/python
#coding: utf-8

import turtle as tu
from turtle import Turtle
from kamlib import *

p1 = obj(color = "red", drawstep  = 500, x = 0.8*AU, vy = 70*kms, charges = [charge(value = 1* 10**32, type = mass)])
p2 = obj(color = "blue", drawstep  = 500, x = -0.8*AU, vy = -70*kms, charges = [charge(value = 1 * 10**32, type = mass)])

ast = obj(color = "blue", drawstep  = 500, x = 0.9*AU, vy = 800*kms, charges = [charge(value = 10**10, type = mass)])


#dwie planety kr¹¿¹ wokó³ wspólnego œrodka masy, widac zmiany, gdy masy przestaj¹ byc równe

abc = domain(scale = 10**(-9))
abc.add_obj(p1)
abc.add_obj(p2)
#abc.add_obj(ast)

abc.anim(dt = 30, steps = 1000000)