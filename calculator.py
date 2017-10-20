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
                return (-a / b);
