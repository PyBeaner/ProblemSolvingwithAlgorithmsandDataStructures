__author__ = 'PyBeaner'
from stack import Stack


def divide_by_2(dec_number):
    return base_converter(dec_number, 2)


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while dec_number:
        m, n = dec_number // base, dec_number % base
        s.push(n)
        dec_number = m

    binary_str = ""
    while not s.is_empty():
        binary_str += str(digits[s.pop()])
    return binary_str


if __name__ == '__main__':
    binary_str = divide_by_2(256)
    print(binary_str)

    print(base_converter(15 * 15, 16))
    print(base_converter(8 * 10, 8))
