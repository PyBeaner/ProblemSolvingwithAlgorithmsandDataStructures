__author__ = 'PyBeaner'
from stack import Stack


def divide_by_2(dec_number):
    s = Stack()
    n = 0
    while dec_number:
        m, n = dec_number // 2, dec_number % 2
        s.push(n)
        dec_number = m

    binary_str = ""
    while not s.is_empty():
        binary_str += str(s.pop())
    return binary_str


if __name__ == '__main__':
    binary_str = divide_by_2(256)
    print(binary_str)
