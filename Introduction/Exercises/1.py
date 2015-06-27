# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison
#   operators (< , >)
from fractions import gcd

"""
def gcd(m,n):
    while n:
        m,n = n,m%n
    return m
"""


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den

        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    print(x + y)
    print(x == y)
