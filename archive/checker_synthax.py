# ret deparated data with different char and keep char in format
def extend_split_preserve_sep(data, sep):
        tmp = ''
        l = list()
        for _ in range(0, len(data)):
                if (len(tmp) > 1 and (data[_] in sep or _ + 1 == len(data))):
                        if (_ + 1 == len(data)):
                                tmp += data[_]
                        l.append(tmp)
                        tmp = ''
                tmp += data[_]
        return (l)


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


test = '5 * X^0.0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 18.6 * X^2'
ret = main_synthax_checker('5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 18.6 * X^2')
if (ret):
	print ("Success.")
else:
	print ("Failed.")
