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
        assert isinstance(top, int), "the numerator should be an integer"
        assert isinstance(bottom, int), "the denominator should be an integer"
        assert bottom != 0, "the denominator should not be zero"
        # allow negative denominator
        if top / bottom < 0:
            top = -abs(top)
            bottom = abs(bottom)
        self.num = top
        self.den = bottom
        self._common = gcd(self.num, self.den)

    @property
    def lowest_num(self):
        return self.num // self._common

    @property
    def lowest_den(self):
        return self.den // self._common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        new_num = self.lowest_num * other.lowest_den + self.lowest_den * other.lowest_num
        new_den = self.lowest_den * other.lowest_den

        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        other = Fraction(-other.num, other.den)
        return self + other

    def __mul__(self, other):
        new_num = self.lowest_num * other.lowest_num
        new_den = self.lowest_den * other.lowest_den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        other = Fraction(other.den, other.num)
        return self * other

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self == other or self > other

    def __lt__(self, other):
        return not self > other

    def __le__(self, other):
        return self == other or self < other

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __ne__(self, other):
        return not self == other

    """
    Implement the simple methods get_num and get_den that will return the numerator
        and denominator of a fraction."""

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    # False
    print(x == y)
    print(x > y)
    print(x >= y)
    # True
    print(x < y)
    print(x <= y)
    print(x != y)

    # x = Fraction(1.0, 1)
    x = Fraction(1, -1)
    print(x)
    # x = Fraction(1,0)
