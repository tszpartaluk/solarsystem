# !/usr/bin/python
#coding: utf-8

import turtle as tu
from turtle import Turtle
from kamlib import *

r = 50

rot_net(rad = 1000, rays = 12, step = 50, circles = 20, color = "lightgray")

mass = chargetype(typ = 'mass', constant = 10)	#definiowanie typu ³adunku: mass
#definiowanie obiektów
kam = obj(drawstep = 500, color = 'blue', x = 200, y = 0, vy = 30, charges = [charge(value = 100000, type = mass)])
kam1 = obj(drawstep = 500, color = 'red', x = 230, y = 0, vy = 170, charges = [charge(value = 1000, type = mass)])

#definiowanie nieruchomego pola centralnego
a = forcefield_central(x = 0, y = 0, charge = charge(value = 50000, type = mass))

#rysowanie ko³a, zielaze¿ne od kamlib
rot_net(rad = 0, rays = 1, step = 50, circles = 1, color = "black")

#definiowanie domeny abc
abc = domain( ffd = [a])

#dodawanie wczesniej utworzonych obiektów do domeny
abc.add_obj(kam)
abc.add_obj(kam1)
t = 0.00007
#rysowanie kropek w miejscach pól centralnych istniej¹cych w domenie abc
abc.show_cfields()

print abc.dsou
abc.anim(dt = t, steps = 10000000)	#odpalanie animacji