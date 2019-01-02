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

import sys

# a : x2
# b : x
# c : 1 

class Calculator:
        def calc_discr(self, a, b, c):
                return (b * b - 4 * a * c)

        def calc_x1(self, delta, a, b, c):
                return (-b + self.sqrt(delta)) / (2 * a)

        def calc_x2(self, delta, a, b, c):
                return (-b - self.sqrt(delta)) / (2 * a)

        def calc_x(self, a, b):
                return (-b / (2 * a))

        def calcul_polynome1(self, a, b):
                return (-a / b);

	def sqrt(self, nb):
		nb = float(nb)
		x, y = 1, nb
		while (abs(y - x) > 0.00000000001):
			x, y = (x + y) / 2, nb / x
		return (x)

class Polynome_deg_2:
	def __init__(self, data):
		self.error = 0
        	self.discr = 0.0
        	self.x1, self.x2 = 0.0, 0.0
        	self.right_member, self.left_member, self.main_member = {}, {}, {}
		self.init_data = data
		self.polynomial_degree = 0

	def found_polynomial_degree(self):
		for key, value in self.main_member.items():
			if (value != 0.0):
				self.polynomial_degree = key

	def found_type_power(self, data):
		if (len(data) == 2):
			data = data[1]
			type_power = (data.split('^'))
			return (int(type_power[1]))
		return (0)

	def parsing_member(self, data):
		member = {}
		data = extend_split_preserve_sep(data, '+-')
		for i in data:
			tmp2 = i.split('*')
			tt = float(tmp2[0].replace(' ', '').replace('+',''))
			member[self.found_type_power(tmp2)] = tt
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
			self.x1 = calc_x(self, a, b)

	def calcul_polynome_gen(self):
		if (self.polynomial_degree == 2):
			self.calcul_polynome()
		elif (self.polynomial_degree == 1):
			print (self.main_member)
			if (self.main_member[1] == 0.0):
				if (self.main_member[0] == 0.0):
					print ("Equation indeterminee")
				else:
					print ("Equation ympossible")
			else:
				self.x1 = Calculator().calcul_polynome1(self.main_member[0], self.main_member[1])
		else:
			print (self.main_member.items()[0])
			if (len(self.main_member.items())== 1 and self.main_member.items()[0] == (0, 0.0)):
				print ("Equation indetermine.")
			else:
				print ("Equation impossible")

	def processing_calcul(self):
		if (main_synthax_checker(self.init_data)):
			self.parsing()
			self.found_polynomial_degree()
			self.calcul_polynome_gen()
		else:
			print ("Synthax error: " + self.init_data)
			self.error = 1

	def display_member(self, data):
		string = ''
		c = 0
		if (data.items()[0][1] < 0.0):
			string += '-'
		for key, value in data.items():
			string += str(abs(value)) + " * X^" + str(key)
			if (c < len(data) - 1):
				string += {True: " + ", False: " - "}[data.items()[c + 1][1] >= 0.0]
			c += 1
		string += (' = 0')
		return (string)

	def display_solution(self):
		data = ''
		if (self.polynomial_degree == 2):
			if (self.discr > 0):
				data += str(self.x1) + '\n' + str(self.x2)
			elif(self.discr == 0):
				data += str(self.x1)
			else:
				data += ("No solution : discriminant < 0.")
		elif (self.polynomial_degree > 2):
				data += "The polynomial degree is stricly greater than 2, I can't solve."			
		elif (self.polynomial_degree == 1):
				data += str(self.x1)
		return (data)

	def __str__(self):
		self.found_polynomial_degree()
		data = 'Form inital: ' + str(self.init_data)
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
        return (l)

class Test_framework:
	l = list()

	def test_function(self, data):
        	c = Polynome_deg_2(data)
        	c.processing_calcul()
        	print (c)
        	print ("\n---------\n\n")

	def append(self, data):
		self.l.append(data)

	def test(self):
		for i in self.l:
			self.test_function(i)


#check all caratcer in string if same sep
def synthax_character_checker(data, sep):
	print ("check data : " + data)
	for i in data:
		print ("check : " + str(i))
		if i not in sep:
			print ("Ret zero error bitches")
			return (0)
	return (1)

def synthax_string_check(data):
	if (data.count('=') != 1):
		return (1)
	return (0)

def process_str(data):
	c = Polynome_deg_2(data)
	c.processing_calcul()
	if (c.error == 0):
		print (c)

def main_process():
	size = len(sys.argv)
	c = 1
	if (size == 1):
		data = raw_input("Data: ")
		if (main_synthax_checker(data)):
			process_str(data)
		else:
			print ("FUCKING ERROR.\n")
		return
	while (c < size):
		process_str(sys.argv[c])
		c += 1

#######
## synthax checker
#######
def synthax_character_checker(data, sep):
        for i in data:
                if i not in sep:
                        return (0)
        return (1)

# check good power or not
def check_power(data):
        ret = data.find('X^', 0, 2)
        if (ret == 0):
                data = data[2:]
                for _ in data:
                        if ((_ < '0' or _ > '9')):
                                return (0)
        return (1)

# check good number or not
def check_number(data):
        c = 0

        if (data[0] == '-' or data[0] == '+'):
                c += 1
        while c < len(data):
                if ((data[c] < '0' or data[c] > '9') and (data[c] != '.')):
                        return (0)
                c += 1
        return (1)

# trouver le type de donnee
def check_good_synthax_or_not(data):
        my = data.split(' ')
        number, power, add_sub, error = 0, 0, 0, 0
        for i in my:
                if (len(i) == 0 or (len(i) == 1 and (i[0] == '+' or i[0] == ' ' or i[0] == '-'))):
                        if (len(i) == 0):
                                add_sub = 0
                        elif (i[0] == '+' or i[0] == '-'):
                                add_sub += 1
                elif (synthax_character_checker(i, " +-.0123456789")):
                        if (check_number(i)):
                                number += 1
                        else:
                                error += 1
                elif (synthax_character_checker(i, "X^0123456789")):
                        if (check_power(i)):
                                power += 1
                        else:
                                error += 1
                elif ('*' != i[0] or len(i) > 1):
                        error += 1
        if (error == 0 and power == 1 and number == 1):
                return (1)
        return (0)

def main_synthax_checker(dat):
        data = dat.split('=')
        if (len(data) != 2):
                return (0)
        m1, m2 = extend_split_preserve_sep(data[0], '-+'), extend_split_preserve_sep(data[1], '-+')
        for i in m1:
                ret = check_good_synthax_or_not(i)
                if (ret == 0):
                        return (0)
        for i in m2:
                ret = check_good_synthax_or_not(i)
                if (ret == 0):
                        return (0)
        return (1)

main_process()

test1 =                       "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0"
test2 =                       "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
test3 =                       "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 18.6 * X^2"
test4 =                       "-10 * X^0 + 3 * X^1 + 1 * X^2 = 0" # 2 and -5
test_invalid_polynome =       "5 * X^0 + 4 * X^1 + 9.3 * X^2 + 5.2 * X^5 = 1 * X^0"
test_invalid_polynome2 =      "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 10 * X^5"
test_polynome_1 =             "5 * x^0 + 2 * X^1 = 0"
test_polynome_1_indetermine = "0 * x^0 + 0 * X^1 = 0"
test_polynome_1_impossible =  "10 * x^0 + 0 * X^1 = 0"
test_fake_polynome_2 =        "5 * X^0 + 4 * X^1 + 0 * X^2 = 0"
test_puiss_0_without_power_notation = "5 + 5 * X^1 + 2 * X^2 = 0" 
test_0 = "0 = 0"
test_empty_str = ""

#test = Test_framework()
#test.append(test1)
#test.append(test2)
#test.test()

'''
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

print ("--------\n\n")

p = Polynome_deg_2(test_fake_polynome_2)
p.processing_calcul()
print (p)

print ("-------\n\n")

z = Polynome_deg_2(test_puiss_0_without_power_notation)
z.processing_calcul()
print(z)
'''

