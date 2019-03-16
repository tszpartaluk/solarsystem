# !/usr/bin/python
#coding: utf-8

import turtle as tu
from turtle import Turtle
from kamlib import *

r = 50

mass = chargetype(typ = 'mass', constant = 10)	#definiowanie typu ³adunku: mass
#definiowanie obiektów
kam = obj(drawstep = 500, color = 'blue', x = 200, y = 0, vy = 30, charges = [charge(value = 100000, type = mass)])
kam1 = obj(drawstep = 500, color = 'red', x = 230, y = 0, vy = 200, charges = [charge(value = 1000, type = mass)])
kam2 = obj(drawstep = 500, color = 'green', x = 240, y = 0, vy = 195, charges = [charge(value = 10, type = mass)])

#definiowanie nieruchomego pola centralnego
a = forcefield_central(x = 0, y = 0, charge = charge(value = 50000, type = mass))

#rysowanie ko³a, zielaze¿ne od kamlib
tu.penup()
tu.goto(0,r)
tu.setheading(180)
tu.pd()
tu.circle(r)

#definiowanie domeny abc
abc = domain( ffd = [a])

#dodawanie wczesniej utworzonych obiektów do domeny
abc.add_obj(kam)
abc.add_obj(kam1)
abc.add_obj(kam2)
t = 0.00005
#rysowanie kropek w miejscach pól centralnych istniej¹cych w domenie abc
abc.show_cfields()

print abc.dsou
abc.anim(dt = t, steps = 10000000)	#odpalanie animacji