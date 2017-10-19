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
	def calc_discr(self, a, b, c):
		return (b * b - 4 * a * c)

	def calc_x1(self, delta, a, b, c):
		return (-b + math.sqrt(delta)) / (2 * a)

	def calc_x2(self, delta, a, b, c):
		return (-b - math.sqrt(delta)) / (2 * a)

	def calc_x(self, a, b):
		return (-b / (2 * a))

	def calcul_polynome1(self, a, b):
		print ("Process data  : " + str(b) + "*X + " + str(a))
		return (-a / b);

# a : x2
# b : x
# c : 1 

class Polynome_deg_2:
	def __init__(self, data):
        	self.discr = 0.0
        	self.x = 0.0
        	self.x1 = 0.0
        	self.x2 = 0.0
        	self.right_member = {}
        	self.left_member = {}
        	self.main_member = {}
		self.init_data = data
		self.polynomial_degree = 0

	def found_polynomial_degree(self):
		self.polynomial_degree = (self.main_member.items()[len(self.main_member.items()) - 1][0])

	def found_type_sqrt(self, data):
		type_sqrt = (data.split('^'))
		number = int(type_sqrt[1])
		return (number)

	def parsing_member(self, data):
		member = {}
		dat = data.split('+')
		data = extend_split_preserve_sep(data, '+-')
		for i in data:
			tmp = i.split('*')
			for ii in tmp:
				tmp2 = i.split('*')
				tt = float(tmp2[0].replace(' ', '').replace('+',''))
				member[self.found_type_sqrt(tmp2[1])] = float(tt)#float(tmp2[0])
		return (member)

	def add_two_member(self):
		for _ in self.right_member:
			self.main_member[_] = self.right_member[_]	
		for key, value in self.left_member.items():
			if key in self.main_member:
				self.main_member[key] -= self.left_member[key]
			else:
				self.main_member[key] = -(self.left_member[key])

	def parsing(self):
		all_member = self.init_data.split('=')
		if len(all_member) < 2:
			print ("error")
			return ("bibitch")
		self.right_member = self.parsing_member(all_member[0])
		self.left_member = self.parsing_member(all_member[1])
		self.add_two_member()

	# found result of 2 degree polynome
	# stock in x, x1, x2
	def calcul_polynome(self):
		self.discr = Calculator().calc_discr(self.main_member[0], self.main_member[1], self.main_member[2])
		if (self.discr > 0):
			self.x1 = Calculator().calc_x1(self.discr, self.main_member[2], self.main_member[1], self.main_member[0])
			self.x2 = Calculator().calc_x2(self.discr, self.main_member[2], self.main_member[1], self.main_member[0])

		elif (self.discr == 0):
			x = calc_x(self, a, b)

	def calcul_polynome_gen(self):
		if (self.polynomial_degree == 2):
			self.calcul_polynome()
		elif (self.polynomial_degree == 1):
			if (self.main_member[1] == 0.0):
				if (self.main_member[0] == 0.0):
					print ("Equation indeterminee")
				else:
					print ("Equation impossible")
			else:
				Calculator().calcul_polynome1(self.main_member[0], self.main_member[1])
		else:
			print ("Equation impossible")

	#http://algor.chez.com/math/eq2deg.htm

	def processing_calcul(self):
		print ("Parsing :")
		self.parsing()
		print ("Found polynomial degree:")
		self.found_polynomial_degree()
		print ("Calcul Poly : " + str(self.polynomial_degree))
		self.calcul_polynome_gen()
		print ("End processing_calcul")

	def display_member(self, data):
		string = ''
		c = 0
		if (data.items()[0][1] < 0.0):
			string += '-'
		for key, value in data.items():
			string += str(abs(value)) + " * X^" + str(key)
			if (c < len(data) - 1):
				if (data.items()[c + 1][1] >= 0.0):
					string += (" + ")
				else:
					string += (" - ")
			c += 1

		string += (' = 0')
		return (string)

	def display_solution(self):
		data = ''
		if (self.polynomial_degree == 2):
			if (self.discr > 0):
				data += str(self.x1) + '\n' + str(self.x2)
			elif(self.discr == 0):
				data += str(self.x)
			else:
				data += ("No solution : discr --> " + str(self.discr))
		elif (self.polynomial_degree > 2):
				data += "The polynomial degree is stricly greater than 2, I can't solve."			
		return (data)

	def __str__(self):
		self.found_polynomial_degree()
		data = ''
		data += 'Form inital: ' + str(self.init_data)
		data += '\nReduced form: ' + self.display_member(self.main_member)
		data += '\nPolynomial degree: ' + str(self.polynomial_degree) + '\n'
		data += self.display_solution()
		return (data)

# ret deparated data with different char and keep char in format
def extend_split_preserve_sep(data, sep):
        tmp = ''
        l = list()
        for _ in range(0, len(data)):
                # len is for begining of str
                # check if actual char is present is list of sep data
                if (len(tmp) > 1 and (data[_] in sep or _ + 1 == len(data))):
			if (_ + 1 == len(data)):
				tmp += data[_]
                        l.append(tmp)
                        tmp = ''
                tmp += data[_]
        tmp = ''
        return (l)

test1 =                       "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0"
test2 =                       "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
test3 =                       "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 18.6 * X^2"
test4 =                       "-10 * X^0 + 3 * X^1 + 1 * X^2 = 0" # 2 and -5
test_invalid_polynome =       "5 * X^0 + 4 * X^1 + 9.3 * X^2 + 5.2 * X^5 = 1 * X^0"
test_invalid_polynome2 =      "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 10 * X^5"
test_polynome_1 =             "5 * x^0 + 2 * X^1 = 0"
test_polynome_1_indetermine = "0 * x^0 + 0 * X^1 = 0"
test_polynome_1_impossible =  "10 * x^0 + 0 * X^1 = 0"

c = Polynome_deg_2(test1)
c.processing_calcul()
print (c)

print ("\n--------\n\n")

d = Polynome_deg_2(test2)
d.processing_calcul()
print (d)

print ("\n--------\n\n")

e = Polynome_deg_2(test3)
e.processing_calcul()
print (e)

print ("\n--------\n\n")

f = Polynome_deg_2(test4)
f.processing_calcul()
print (f)

print ("\n--------\n\n")

r = Polynome_deg_2(test_invalid_polynome)
r.processing_calcul()
print (r)

print ("\n--------\n\n")

r = Polynome_deg_2(test_invalid_polynome2)
r.processing_calcul()
print (r)

print ("\n-------\n\n")

p = Polynome_deg_2(test_polynome_1)
p.processing_calcul()
print (p)

print ("--------\n\n")

p = Polynome_deg_2(test_polynome_1_indetermine)
p.processing_calcul()
print (p)

print ("--------\n\n")

p = Polynome_deg_2(test_polynome_1_impossible)
p.processing_calcul()
print (p)
#print (c)
#print (c.discr)
#print (c.x)
#print (c.x1)
#print (c.x2)


#print (extend_split_preserve_sep("coucou toi - salope + is her mother fucking bitches", "+-"))
#print (extend_split_preserve_sep("5 * X^0 + 4 * X^1 - 9.3 * X^2", "+-"))
