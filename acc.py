# !/usr/bin/python
#coding: utf-8

import turtle as tu
from turtle import Turtle
from kamlib import *

r = 50

mass = chargetype(typ = 'mass', constant = 10)	#definiowanie typu ³adunku: mass

#definiowanie obiektów
p1 = rocket(massive = False, drawstep = 1000, color = 'blue', x = 200, y = 0, vy = 50, charges = [charge(value = 1000, type = mass)])
sat = obj(massive = False, drawstep = 500, color = 'red', x = 100, y = 0, vy = 50*1.41, charges = [charge(value = 1, type = mass)])

#definiowanie nieruchomego pola centralnego
a = forcefield_central(x = 0, y = 0, charge = charge(value = 50000, type = mass))

#rysowanie siatki
rot_net(rad = 1000, rays = 12, step = 50, circles = 20, color = "lightgray")

#rysowanie ko³a
rot_net(rad = 0, rays = 1, step = 50, circles = 1, color = "black")



#definiowanie domeny abc
abc = domain( ffd = [a])

#dodawanie wczesniej utworzonych obiektów do domeny
#abc.add_obj(p1)
abc.add_obj(sat)
t = 0.00015
#rysowanie kropek w miejscach pól centralnych istniej¹cych w domenie abc
abc.show_cfields()



print abc.dsou
abc.anim(dt = t, steps = 30000)	#odpalanie animacji



abc.objects[0].set_color('blue')

duration = 50000
singlestep = 1000

acc1 = 1.005

for a in range(duration/singlestep):

	abc.objects[0].vy = abc.objects[0].vy*acc1
	abc.objects[0].vx = abc.objects[0].vx*acc1
	abc.anim(dt = t, steps = singlestep)


abc.anim(dt = t, steps = 70000)

acc2 = 1.4

abc.objects[0].vy = abc.objects[0].vy*acc2
abc.objects[0].vx = abc.objects[0].vx*acc2

abc.objects[0].set_color('red')

abc.anim(dt = t, steps = 500000)