"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""


class Quaternion:

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return f'({repr(self.a)}, {repr(self.b)}, {repr(self.c)}, {repr(self.d)})'

    def __str__(self):
        return f'{self.a:.3f} {self.b:+.3f}i {self.c:+.3f}j ' \
               f'{self.d:+.3f}k'

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        d = self.d + other.d
        sum = Quaternion(a, b, c, d)
        return sum

    def __mul__(self, other):
        a = (other.a * self.a - other.b * self.b - other.c * self.c - other.d * self.d)
        b = (other.a * self.b + other.b * self.a - other.c * self.d + other.d * self.c)
        c = (other.a * self.c + other.b * self.d + other.c * self.a - other.d * self.b)
        d = (other.a * self.d - other.b * self.c + other.c * self.b + other.d * self.a)
        mul = Quaternion(a, b, c, d)
        return mul

    def __truediv__(self, other):
        inverse_a = other.a / other.sum_of_squares()
        inverse_b = -other.b / other.sum_of_squares()
        inverse_c = -other.c / other.sum_of_squares()
        inverse_d = -other.d / other.sum_of_squares()

        other_inverse = Quaternion(inverse_a, inverse_b, inverse_c, inverse_d)
        return self * other_inverse

    def __abs__(self):
        return self.sum_of_squares() ** 0.5

    def __eq__(self, other):
        return self.__abs__() == other.__abs__()

    def sum_of_squares(self):
        return self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2


quaternion1 = Quaternion(1, 2, 3, 4)
quaternion2 = Quaternion(4, 3, 2, 1)
sum = quaternion1 + quaternion2
mul = quaternion1 * quaternion2
dell = quaternion1 / quaternion2
quaternion3 = abs(quaternion1)
print(sum)
print(mul)
print(dell)
