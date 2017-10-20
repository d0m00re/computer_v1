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

test = "5 * X^0 + 4 * X^1 + 9.3 * X^2 = 1 * X^0 + 18.6 * X^2"

data = test.split('=')

m1 = extend_split_preserve_sep(data[0], '-+')
m2 = extend_split_preserve_sep(data[1], '-+')

print('')
print (m1)
print('')
print (m2)
