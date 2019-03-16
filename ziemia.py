# !/usr/bin/python
#coding: utf-8

import turtle as tu
from turtle import Turtle
from kamlib import *

r = 50
#AU = 149597887000	#jednostka astronomiczna w metrach
kms = 1000

mass = chargetype(typ = 'mass', constant = G)

#mass = chargetype(typ = 'mass', constant = 10)	#definiowanie typu ³adunku: mass
#definiowanie obiektów

zie = obj(drawstep = 1000, color = 'blue', x = AU*0.983, y = 0, vy = 30.29*kms, charges = [charge(value = 5.9736*(10**24), type = mass)])
moon = obj(drawstep = 500, color = 'red', x = AU*(0.983 + 0.0025), y = 0, vy = (30.290 + 1.8)*kms, charges = [charge(value = 7.347*10**22, type = mass)])

merk = obj(drawstep = 1000, color = 'blue', x = AU*0.30749951, y = 0, vy = 58980, charges = [charge(value = 3.3302*(10**23), type = mass)])

#definiowanie nieruchomego pola centralnego, tutaj s³oñca
sun = forcefield_central(x = 0, y = 0, charge = charge(value = 1.9891*(10**30), type = mass))


#rysowanie ko³a, zielaze¿ne od kamlib
tu.penup()
tu.goto(0,r)
tu.setheading(180)
tu.pd()
tu.circle(r)

#definiowanie domeny abc
abc = domain(scale = 2*10**(-9), dsou = [0,1], ffd = [sun])

#dodawanie wczesniej utworzonych obiektów do domeny
abc.add_obj(zie)
#abc.add_obj(merk)
abc.add_obj(moon)
t = 120.0
#rysowanie kropek w miejscach pól centralnych istniej¹cych w domenie abc
abc.show_cfields()
abc.anim(dt = t, steps = 10000000)	#odpalanie animacji