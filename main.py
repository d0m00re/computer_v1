# $>./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
# Polynomial degree: 2
# Discriminant is strictly positive, the two solutions are:
# 0.905239
# -0.475131
# $>./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
# Reduced form: 1 * X^0 + 4 * X^1 = 0
# Polynomial degree: 1
# The solution is:
# -0.25
# ./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
# Polynomial degree: 3
# The polynomial degree is stricly greater than 2, I can't solve.

# Polynome deg2:
# ax^2 + bx + c = 0

# SOLVER
# 1) calcul delta:
#	delta = b * b - 4 * a * c
# si d > 0:
# 	x1 = (-b + sqrt(delta)) / (2 * a)
#	x2 = (-b - sqrt(delta)) / (2 * a)
#
# si d == 0:
#	x = -b/2a
#
# si d < 0 : pas de solution possible:

import math

class Calculator:
	def add(self, a, b):
		return (a + b)

	def sub(self, a, b):
		return (a - b)

	def mult(self, a, b):
		return (a * b)

	def div(self, a, b):
		return (a / b)

	def calc_discr(self, a, b, c):
		return (b * b - 4 * a * c)

	def calc_x1(self, delta, a, b, c):
		return (-b + math.sqrt(delta)) / (2 * a)

	def calc_x2(self, delta, a, b, c):
		return (-b - math.sqrt(delta)) / (2 * a)

	def calc_x(self, a, b):
		return (-b / (2 * a))

	def basic_calcul(self, string):
		data = string.split(" ")
		nb1, nb2 = float(data[0]), float(data[2])
		if (data[1] == '+'):
			return (self.add(nb1, nb2))
		elif (data[1] == '-'):
			return (sub(nb1, nb2))
		elif (data[1] == '/'):
			return (div(nb1, nb2))
		elif (data[1] == '*'):
			return (mult(nb1, nb2))

	def basic_calcul2(self, string):
		return eval(string)

#>>> mon_dictionnaire = {}
#>>> mon_dictionnaire["pseudo"] = "Prolixe"
#>>> mon_dictionnaire["mot de passe"] = "*"
#>>> mon_dictionnaire
#{'mot de passe': '*', 'pseudo': 'Prolixe'}
#>>>

# a : x2
# b : x
# c : 1 

class Polynome_deg_2:
	#discr = 0.0
	#x = 0.0
	#x1 = 0.0
	#x2 = 0.0
	#init_data = ''
	#right_member = {}
	#left_member = {}
	#main_member = {}

	def __init__(self, data):
        	self.discr = 0.0
        	self.x = 0.0
        	self.x1 = 0.0
        	self.x2 = 0.0
        	self.right_member = {}
        	self.left_member = {}
        	self.main_member = {}
		self.init_data = data

	def found_type_sqrt(self, data):
		type_sqrt = (data.split('^'))
		print (type_sqrt[1])
		number = int(type_sqrt[1])
		return (number)

	def parsing_member(self, data):
		member = {}
		data = data.split('+')
		for i in data:
			tmp = i.split('*')
			for ii in tmp:
				tmp2 = i.split('*')
				member[self.found_type_sqrt(tmp2[1])] = float(tmp2[0])
		return (member)

	def add_two_member(self):
		for _ in self.right_member:
			self.main_member[_] = self.right_member[_]
		for _ in self.left_member:
			if self.main_member[_]:
				self.main_member[_] -= self.left_member[_]
			else:
				self.main_member[_] = -(self.left_member[_])

	def parsing(self):
		all_member = self.init_data.split('=')
		if len(all_member) < 2:
			print ("error")
			return ("bibitch")
		self.right_member = self.parsing_member(all_member[0])
		self.left_member = self.parsing_member(all_member[1])
		self.add_two_member()
		print (self.right_member)
		print (self.left_member)

	def calcul_poly(self):
		self.discr = Calculator().calc_discr(self.main_member[0], self.main_member[1], self.main_member[2])
		if (self.discr > 0):
			self.x1 = Calculator().calc_x1(self.discr, self.main_member[2], self.main_member[1], self.main_member[0])
			self.x2 = Calculator().calc_x2(self.discr, self.main_member[2], self.main_member[1], self.main_member[0])

		elif (self.discr == 0):
			x = calc_x(self, a, b)

	def processing_calcul(self):
		self.parsing()
		self.calcul_poly()

	def __str__(self):
		data = ''
		data += 'Form inital: ' + str(self.init_data)
		data += '\nReduced form: ' + str(self.main_member) 
		return (data)


test1 = "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0"
test2 = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
test3 = "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 18.6 * X^2"

c = Polynome_deg_2(test3)
c.processing_calcul()

print (c)
print (c.discr)
print (c.x)
print (c.x1)
print (c.x2)
