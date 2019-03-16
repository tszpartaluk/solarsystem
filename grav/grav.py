# !/usr/bin/python
#coding: utf-8

import turtle as tu
from turtle import Turtle
import math
from math import fabs

AU = 149597887000 #metrów
G = 6.67384808080808*10**(-11)	#sta³a grawitacji
kms = 1000	#konwersja na metry na sekundê
pi = math.pi
e = math.e
kg = 1.0
km = 1000.0	#konwersja na metry


class ffield_central:
	def __init__(self, const = G, mass = 1.0):
	
		self.mass = float(mass)
		self.x = float(x)
		self.y = float(y)
		
	def acc(self, object):
	
		if (object.x == self.x) and (object.y == self.y) :
			return [0.0,0.0]
			
		delx = self.x - object.x
		dely = self.y - object.y
	
		acc = G*self.mass/((delx**2 + dely**2)**(3.0/2))
		
		return [delx*acc, dely*acc]

		
class obj:
	def __init__(self, mass = 1.0, x = 0.0, y = 0.0, vx = 0.0, vy = 0.0, massive = True, drawstep = 1, color = 'black'):
	
		self.mass = float(mass)
		self.x = float(x)
		self.y = float(y)
		self.vx = float(vx)
		self.vy = float(vy)
		
		self.massive = massive
		#czesc odpowiedzialna za rysowanie œcie¿ki
		self.path = Turtle()
		self.path.speed(0)
		self.path.hideturtle()
		self.path.color(color)

	def id(self):
		return 'obj'
		
class domain:
	def __init__(self, ffields = [], x = 0.0, y = 0.0):
	
		self.ffields = ffields
		self.objects = []
		self.ffields_dyn = []
		
	def add_obj(self, _new):
		try:
			if (_new.id() == 'obj'):

				self.objects.append(_new)
				if _new.massive == True:

					self.ffields_dyn.append(len(self.objects)-1)
					self.report("Nowy masywny obiekt dodany", "obiekty w bazie:\t" + str(len(self.objects)))
				else:
					self.report("Nowy lekki obiekt dodany", "obiekty w bazie:\t" + str(len(self.objects)))	
			else:
				self.report("ERROR, niepoprawny obiekt")
		except AttributeError:
			self.report("ERROR, niepoprawny obiekt")
		
		
	def report(self, *args):
	
	
		for i in range(len(args)):
			print args[i]