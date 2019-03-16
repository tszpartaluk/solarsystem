# !/usr/bin/python
#coding: utf-8

###########################################################
#
# KAMLIB.PY
#
# WERSJA:09.12.2012 dnia:22:57
#
###########################################################

import turtle as tu
from turtle import Turtle
import math
from math import fabs

#STA�E FIZYCZNE W UK�ADZIE SI

AU = 149597887000 #metr�w
G = 6.67384808080808*10**(-11)	#sta�a grawitacji
kms = 1000	#konwersja na metry na sekund�
pi = math.pi
e = math.e
E0 = 8.841941283*(10**(-12))	#sta�a dielektryczna pr�ni
kg = 1.0
km = 1000.0	#konwersja na metry
k = 1/(4*pi*E0)




#def coord(type = "kartezjan")

#wszystkie warto�ci wy�szego rz�du ni� domeny
class world:
	def __init__(self, nazwa = 'witaj w rzucie kamieniem', echo = True):
		self.echo = True
		self.domains = 0
		self.charges = 0
		self.charge_typs = []
		self.charge_units = []
		
		self.clock = 0
		
		self.nazwa = nazwa
		tu.hideturtle()
		tu.title(self.nazwa)
		tu.speed(0)
		self.fresh = True
		self.echo = True

	#ustawienia raport�w
	def echo(self, echo):
		if echo == False:
			self.echo = False
		else:
			self.echo = True
			
	#wyrzucanie komunikat�w do konsoli
	def report(self, *args):
	
		if self.echo == True: 
			rep = 0
			for rep in args:
					print "World", '\t\t' + str(rep)
	
	#zmiana nazwy okna z grafik�
	def set_window_title(self, nazwa = ''):
	
		tu.title(nazwa)
		self.report("zmieniono nazwe okna na:" + str(nazwa))

	#czy�ci ekran graficzny
	def wyczysc(self):
		tu.clearscreen()
		tu.reset()
		self.__init__(self.nazwa)
		
	#dodawanie domeny
	def add_domain(self, name):
		self.domains +=1
		if(nazwa == '' or nazwa == ""):
			self.report("Domena_" + str(world.domains))
			return ("Domena_" + str(world.domains))
			
		else:
			self.report(nazwa)
			return nazwa
			
	
	#sprawdza czy �adunek o typie "type" istnieje
	def check_charge(self, typ):

		#szukanie w bazie �adunk�w czy istnieje dany �adunek
		for b in range(len(self.charge_typs)):
			if typ == self.charge_typs[b]:
				#jesli istnieje to zwraca True
				return True
				break
		#jesli nie istnieje to zwraca fa�sz
		return False

		
	#dodawanie �adunku
	def add_charge(self, type):
		
		if self.check_charge(type.typ) == False:
			#tworzeie nazwy dla �adunku
			if type.typ == '' or type.typ == "":
				type.typ = "Charge_" + str(self.charges)
			
			#raport o utworzeniu nowego rodzaju �adunku
			self.report("New Charge:\t" + type.typ)
			self.charges += 1
			self.charge_typs.append(type.typ)
			
		return type
		
	def backgr(self, color = 'white'):
		tu.bgcolor(color)

world = world("kamien")

#rodzaj �adunku
class chargetype:
	def __init__(self, typ = "mass", unit = "basic_unit", constant = 1.0):
		self.typ = typ
		self.unit = unit
		self.constant = constant
		self = world.add_charge(self)
		
	def set_constant(self, _new):
		self.constant = _new

mass = chargetype(typ = "mass", unit = "kg", constant = G)	#przyk�adowy rodzaj �adunku

#�adunek, posiada warto��
class charge:
	def __init__(self, type = mass, value = 0.0):

		self.type = world.add_charge(type)
		self.value = value

	#zwraca warto��
	def val(self):
		return self.value
		
	#zwraca sw�j rodzaj (na przyk�ad, �e jest to masa, albo �adunek elektryczny)
	def chargetype(self):
		return self.type.type

unmassed = charge(type = mass, value = 0.0)	#przyk�adowy �adunek

##################################################################################################################
#POLA	
#jednorodne pole
class forcefield_directional:

	def idcustom(self):
		return False
		
	def __init__(self, dx = 0.0, dy = 0.0, type = mass):
		self._cusotm = False
		#sk�adowe nat�enia
		self.dx = dx
		self.dy = dy
		self.type = type
		
		#okre�lanie typu �adunku
		if type.__class__.__name__ == "chargetype" or type.__class__.__name__ == "charge":
			if world.check_charge(type.typ) == True:
				self.type == type
			else:
				self.type = world.add_charge(type)
				
	#zwraca si� jak� diza�a na podany �adunek
	def force(self, charge = unmassed, pos = [0.0,0.0]):
	
		#return [self.dx*charge.value,self.dy*charge.value]
		if charge.type.typ == self.type.typ:
			return [self.dx*charge.value,self.dy*charge.value]
		else:
			return [0.0,0.0]

#pole punktowe
class forcefield_central:	
	def idcustom(self):
		return False
	def __init__(self, x = 0.0, y = 0.0 , charge = unmassed):
		self.x = x
		self.y = y		
		self.charge = charge
		self.type = self.charge.type
		
	#zwraca si�� jak� wywiera na przekazany �adunek
	def force(self, charge = unmassed, pos = [1.0, 1.0]):
		delx = pos[0] - self.x
		dely = pos[1] - self.y
		
		#�eby unikn�� dzielenia przez 0
		if (fabs(delx) + fabs(dely))  == 0:
			return [0., 0.]
		
		rad = (delx**2 + dely**2)**(1.5)
		
		direct = -charge.type.constant*self.charge.value*charge.value/rad
		
		#valx = delx/(rad**0.5)
		#valy = dely/(rad**0.5)
		#print direct, pos[0], pos[1], delx, dely
		return [delx*direct, dely*direct]
	
	def dot(self, turtle = tu):
		turtle.penup()
		turtle.goto(self.x, self.y)
		turtle.pd()
		tutle.dot(5)
		tutle.penup()
	
#klasa do dziedziczenia, kt�ra stanowi baz� dla wszelkich innych p�l kt�rych nie da si� zdefiniowa� za pomoc� ju� istniej�cych
class field_custom:
	def idcustom(self):
		return True
	#zwraca si�� jak� generuje pole
	def force(self, obj):
		return [0,0]
		
##################################################################################################################
#pole wiatru, przyk�ad nietypowego pola zdefiniowanego przez u�ytkownika generuje si�� oporu powietrza		
class windfield(field_custom):
	def __init__(self, vx, vy, d):
		self.vx = vx
		self.vy = vy
		self.d = d
		
	#zwraca si�� z jak� dzia�a na podany obiekt
	def force(self, obj):
	
		v = ((obj.vx-self.vx)**2 + (obj.vy-self.vy)**2)**(0.5)
		
		if v == 0.0:
			return[0.0,0.0]
		
		Fv = self.d * v**2
		
		return [-((obj.vx-self.vx)/v)*Fv,-((obj.vy-self.vy)/v)*Fv]
##################################################################################################################
	
##################################################################################################################		
#okre�la otoczenie
class domain:
	#init
	def __init__(self, scale = 1.0, nazwa = '', dsou = [],ffd = [], customfd = [], echo = True, color = 'black'):
	
	
		self.scale = scale	#skala rysunku
		global world
		self.dsou = []
		self.dffd = []
		#Nadawanie nazwy
		if(nazwa == '' or nazwa == ""):
			self.nazwa = "Domena_" + str(world.domains)
			world.domains += 1
		else:
			self.nazwa = nazwa
			world.domains += 1
		
		#ustawienie raport�w
		self.echo = echo
		
		#self.nazwa = world.add_domain(nazwa)
		world.report(self.nazwa)
		self.report("utworzono domen�")
		
		#w�asny ��w do rysowania
		if(world.fresh == True):
			self.ha = Turtle()
			self.ha.hideturtle()
		
		self.ha.color(color)
		#tablica z obiektami bior�cymi udzia� w obliczeniach domeny
		self.objects = []
		
		#tablica z polami si�owymi w domenie
		self.ffd = []
		for a in range(len(ffd)):
			self.add_field(ffd[a])
			
		#tablica z polami nietypowymi w domenie
		self.customfd = []
		for a in range(len(customfd)):
			self.add_field(customfd[a])
			
		self.Fx = 0.
		self.Fy = 0.

	#w��czanie i wy��czanie raport�w
	def echo(self, echo):
		if echo == False:
			self.echo = False
		else:
			self.echo = True
			
	#wyrzucanie komunikat�w do konsoli, przyjmuje po kilka argument�w
	def report(self, *args):
		
		if self.echo == True: 
			rep = 0
			if(len(self.nazwa) <= 6):
				for rep in args:
					print self.nazwa, '\t\t' + str(rep)
			else:
				for rep in args:
					print self.nazwa, '\t' + str(rep)

	#baza obiekt�w tej domeny
	def add_obj(self, _new):
	
		try:
			if (_new.objecttype() != 'obj'):
				print "ERROR, niepoprawny obiekt"
				self.report("ERROR, niepoprawny obiekt")
			else:
				self.objects.append(_new)
				
				if _new.massive == True:
					self.dsou.append(len(self.objects)-1)
					self.report("Nowy masywny obiekt dodany", "obiekty w bazie:\t" + str(len(self.objects)))
				else:
					self.report("Nowy lekki obiekt dodany", "obiekty w bazie:\t" + str(len(self.objects)))
		except AttributeError:
			self.report("ERROR, niepoprawny obiekt")
				
	#dodaje pole si�owe
	def add_field(self, _new):
		if _new.idcustom() == False:
			self.ffd.append(_new)
			self.report("dodano pole si�owe")
		else:
			self.customfd.append(_new)
			self.report("dodano pole nietypowe")

	#rysuje kropki w miejscach istnienia p�l punktowych
	def show_cfields(self, size = 5):
		
		for a in range(len(self.ffd)):
			if self.ffd[a].__class__.__name__ == 'forcefield_central':
				self.ha.penup()
				self.ha.goto(self.ffd[a].x, self.ffd[a].y)
				self.ha.pd()
				self.ha.dot(size)

	#zwraca tablic� z wektorem wypadkowej wszystkich si� dzia�aj�cych na podany obiekt, kt�rych �r�d�em jest dana domena
	def force(self, obj):
	
	
		self.Fx =0
		self.Fy =0	
		
		###################################################
		#s�y z p�l nietypowych
		Fcufds = []
		for a in range(len(self.customfd)):
			#oddzia�ywanie z polem nietypowym
			Fcufds.append(self.customfd[a].force(obj))
			
		#si�y z p�l si�owych
		Fffds = []
		for a in range(len(self.ffd)):
			#oddzia�ywanie z polem si�owym
			Fffds.append(self.ffd[a].force(charge = obj.return_charge(self.ffd[a].type), pos = obj.pos() ))
			
		##############################################
		#sumowanie si�
		#z p�l nietypowych

		for a in range(len(Fcufds)):
			self.Fx += Fcufds[a][0]
			self.Fy += Fcufds[a][1]
		
		#z p�l si�owych

		for a in range(len(Fffds)):
			self.Fx += Fffds[a][0]
			self.Fy += Fffds[a][1]

		return[self.Fx, self.Fy]

	#uzupe�ina tablic� aktualnymi polami z obiekt�w poruszaj�cych si�
	def fill_dfields(self):
		self.dffd = []
		#ka�dy obiekt po koleji
		for a in self.dsou:
		
			#ka�dy �adunek w obiekcie tworzy pole
			for b in range(len(self.objects[a].charges)):
				#dodanie pola do talbicy ze zmiennymi polami, pochodzi z obiektu dsou[a] wybranego z tablicy dsou i �adunku dsou[a].charges[b] wybranego z tablicy �adunk�w ego obiektu
				self.dffd.append(forcefield_central(x = self.objects[a].x, y = self.objects[a].y, charge = self.objects[a].charges[b]))
		
	#zwraca tablic� z wektorem wypadkowej wszystkich si� dzia�aj�cych na podany obiekt, kt�rych �r�d�em jest dana domena
	def force_dynamic(self, obj):
	
		self.Fx =0
		self.Fy =0	

		###################################################
		#s�y z p�l nietypowych
		Fcufds = []
		for a in range(len(self.customfd)):
			#oddzia�ywanie z polem nietypowym
			Fcufds.append(self.customfd[a].force(obj))
			
		#si�y z p�l si�owych
		Fffds = []
		for a in range(len(self.ffd)):
			#oddzia�ywanie z polem si�owym
			Fffds.append(self.ffd[a].force(charge = obj.return_charge(self.ffd[a].type), pos = obj.pos() ))
			
		Fdffds = []
		self.fill_dfields()
		for a in range(len(self.dffd)):
			#oddzia�ywanie z polem si�owym pochodz�cym z obiektu
			Fffds.append(self.dffd[a].force(charge = obj.return_charge(self.dffd[a].type), pos = obj.pos() ))
		
		##############################################
		#sumowanie si�
		#z p�l nietypowych

		for a in range(len(Fcufds)):
			self.Fx += Fcufds[a][0]
			self.Fy += Fcufds[a][1]
		
		#z p�l si�owych

		for a in range(len(Fffds)):
			self.Fx += Fffds[a][0]
			self.Fy += Fffds[a][1]
			
		#z p�l z obiekt�w
		for a in range(len(Fdffds)):
			self.Fx += Fdffds[a][0]
			self.Fy += Fdffds[a][1]

		return[self.Fx, self.Fy]

		
	#uruchamia sumulacj�, z cz�stk� czasu r�wn� t, symulacja trwa duration czasu, albo jest wykonanych iles krok�w steps, steps maja pierwze�stwo, t nie mo�e si� r�wna� 0
	def anim(self, dt = 0.01, duration = 0, steps = 0, dynamicfields = True, scale = 1.0):
		
		#sprawdzenie czy dt != 0, i czy dt jest 
		try:
			if float(dt) == 0.:
				self.report("Przedzia� czasu r�wny 0!")
		except ValueError:
			self.report("wrong time interval")
			return
		
		self.steps = steps
		#self.report("Anim start...")
		self.dt = float(dt)
		
		dynfds = dynamicfields
		
		if len(self.dsou) == 0:
			dynfds = False
		
		#ustawanie ��wi obiekt�w w pozycjach startowych
		for a in range(len(self.objects)):
			self.objects[a].move_blindturtle(self.scale*self.objects[a].x, self.scale*self.objects[a].y)
	
		#######################################################
		#g��wna p�tla animacji dla domeny
		if dynfds == False:
			self.report("Anim started without dynamic fields...")
			for m in range(self.steps):
				#ka�dy obiekt po koleji
				for n in range(len(self.objects)):
					self.objects[n].move(self, self.force)
				world.clock += 1
		
		elif dynfds == True:
			self.report("Anim started with dynamic fields")
			
			for m in range(self.steps):
				self.fill_dfields()
				#ka�dy obiekt po koleji
				for n in range(len(self.objects)):
					self.objects[n].move(self, self.force_dynamic)
				world.clock += 1
				
		#ustawanie ��wi obiekt�w w pozycjach startowych
		for a in range(len(self.objects)):
			self.objects[a].move_visibleturtle(self.scale*self.objects[a].x, self.scale*self.objects[a].y)
		
		self.report("... anim finished")
	
	#resetuje domen�, nale�y wywo�a� po zresetowaniu �wiata
	def reset(self):
		if(world.fresh == True):
			self.ha = Turtle()
			self.ha.hideturtle()
		self.reset_objects()
	
	#resetuje warto�ci wszystkich obiekt�w w bazie
	def reset_objects(self):
		#komentarz
		for n in range(len(self.objects)):
			self.objects[n].reset()
			
		self.report("obiekty w bazie zresetowane")
		
	def set_color(self, color):
		self.ha.color(color)

##################################################################################################################
#obiekt, punkt, mo�e mie� mas�, �adunek elektryczny, etc.
class obj(object):
	#init
	def __init__(self, vx = 0, vy = 0, x = 0 ,y = 0, charges = [unmassed], fields = [], color = 'black', drawstep = 1, massive = True, path = True, thrust = 0.0):
		
		self.drawstep = drawstep
		self.drawd = 0
		self.charges = []
		self.massive = massive
		#dodawanie �adunk�w
		for a in range(len(charges)):
			self.add_charge(charges[a])
		self.fields = []
		
		if len(fields) != 0:
			for a in range(len(fields)):
				if fields[a] == True:
					self.fields.append(forcefield_central(x = self.x, y = self.y, charge = self.charges[a]))	
		
		#w�a�ciwo�ci obiektu
		self.vx = float(vx)
		self.vy = float(vy)
		self.x = float(x)
		self.y = float(y)
		self.F = 0.0
		
		#��w obiektu
		self.ha = Turtle()
		self.ha.hideturtle()
		self.ha.color(color)
		
		#zapisanie pocz�tkowych warto�ci
		self.save = [self.x, self.y, self.vx, self.vy]
		
		self.rocket_init()

	def rocket_init(self):
		pass
		
	#identyfikator
	def objecttype(self):
		return 'obj'
		
	#dodaje obiektowi �adunek
	def add_charge(self, charg):
	
		#sprawdzenie typu
		if charg.__class__.__name__ == 'charge':
			self.charges.append(charg)
		else:
			#komunikat o b��dzie
			print charg.__class__.__name__, "is not a charge"

	#pozwala na ustalenie nowej pozycji obiektu, uktualnie tez pozycj� ���wia, bez rysowania �ciezki
	def set_pos(self, x, y):
	
		self.x = x
		self.y = y
		
		#zmienia pozycj� z�wia
		self.ha.penup()
		self.ha.speed(0)
		self.ha.goto(self.x, self.y)
		self.ha.pendown()

	#ustawia pr�dko��
	def set_speed(self, vx, vy):
		self.vx = vx
		self.vy = vy
		
	#oblicza nowe po�o�enie na podstawie w�a�ciwo�ci swoich i swojej domeny
	def move(self, domain, forcefun):
	
		#######################################################################
		#rysowanie �cie�ki
		if self.drawd % self.drawstep == 0 or self.drawd == 0:
			self.ha.goto(domain.scale*self.x,domain.scale*self.y)
			#print domain.scale*self.x, domain.scale*self.y
			#print ((self.x**2+self.y**2)*(self.vx**2 + self.vy**2))**(0.5)	#moment p�du
		self.drawd +=1

		#tymczasowa tablica ze sk�adowymi si�y oporu powietrza, po koleji x, y
		self.F = forcefun(self)
		
		#######################################################################
		#	R�WNANIA RUCHU
		
		#nowa wspo�rz�dna x
		self.x = self.x + self.vx*domain.dt + self.F[0]/self.charges[0].value*(domain.dt**2)/2
		#nowa pr�dko�c wzd�u� OX
		self.vx = self.vx + self.F[0]/self.charges[0].value*domain.dt
		
		#nowa wsp�rz�dna y
		self.y = self.y + self.vy*domain.dt + self.F[1]/self.charges[0].value*(domain.dt**2)/2
		#nowa pr�dko�c wzd��z OY
		self.vy = self.vy + self.F[1]/self.charges[0].value*domain.dt
		

		
	#przesuwa ��wia, bez rysowania linii
	def move_blindturtle(self, x, y):
		self.ha.penup()
		self.ha.speed(0)
		self.ha.goto(x, y)
		self.ha.pendown()
		
	#przesuwa ��wia, z rysowaniem linii
	def move_visibleturtle(self, x, y):
		self.ha.pendown()
		self.ha.speed(0)
		self.ha.goto(x, y)

	#zwraca pozycj� obiektu w tablicy [x,y]
	def pos(self):
		return [self.x, self.y]

	#przywraca obiekt do stanu w jakim by� zdefiniowany
	def reset(self):
		self.x = self.save[0]
		self.y = self.save[1]
		self.vx = self.save[2]
		self.vy = self.save[3]
		global world
		if(world.fresh == True):
			self.ha = Turtle()
			self.ha.hideturtle()
	
	#zwraca sw�j �adunek, tego samego rodzaju co podany w argumencie
	def return_charge(self, chargetype):
	
		for a in range(len(self.charges)):
			if self.charges[a].type.typ == chargetype.typ:
				return self.charges[a]
		return unmassed
		
	def set_color(self, color):
		self.ha.color(color)
			
			
class rocket(obj):
	
	def rocket_init(self):
		self.thrust = 0.0
	
	def set_thrust(self, thrust):
		self.thrust = thrust
	
	# def engine(self):
	
		# self.vx
		# return
	
	def pull(self):
		pass
	
	#oblicza nowe po�o�enie na podstawie w�a�ciwo�ci swoich i swojej domeny
	def move(self, domain, forcefun):
	
		#tymczasowa tablica ze sk�adowymi si�y oporu powietrza, po koleji x, y
		self.F = forcefun(self)
		#######################################################################
		#	R�WNANIA RUCHU
		
		#nowa wspo�rz�dna x
		self.x = self.x + self.vx*domain.dt + self.F[0]/self.charges[0].value*(domain.dt**2)/2 + self.thrust/self.m
		#nowa pr�dko�c wzd�u� OX
		self.vx = self.vx + self.F[0]/self.charges[0].value*domain.dt
		
		#nowa wsp�rz�dna y
		self.y = self.y + self.vy*domain.dt + self.F[1]/self.charges[0].value*(domain.dt**2)/2
		#nowa pr�dko�c wzd��z OY
		self.vy = self.vy + self.F[1]/self.charges[0].value*domain.dt
		
		#######################################################################
		#rysowanie �cie�ki
		if self.drawd % self.drawstep == 0:
			self.ha.goto(domain.scale*self.x,domain.scale*self.y)
			#print domain.scale*self.x, domain.scale*self.y
			#print ((self.x**2+self.y**2)*(self.vx**2 + self.vy**2))**(0.5)	#moment p�du
		self.drawd +=1
		
		
def rot_net(x = 0, y = 0, rad = 100, rays = 12, step = 25, circles = 4, color = "black"):

	tu.pencolor(color)
	tu.penup()
	
	for n in range(rays):
	
		tu.goto(x,y)
		tu.seth((360/rays) * n)
		tu.pendown()
		tu.fd(rad)
		tu.penup()
		
	for n in range(circles):
		tu.penup()
		tu.goto(x-(n+1)*(step), y)
		tu.seth(270)
		tu.pd()
		tu.circle((n+1)*step)

