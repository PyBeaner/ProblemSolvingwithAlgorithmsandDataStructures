__author__ = 'PyBeaner'
from stack import Stack


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    for char in symbol_string:
        if char == "(":
            s.push(char)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                s.pop()

    return balanced and s.is_empty()

print(par_checker("(((())))"))
print(par_checker("(((()))"))
print(par_checker("(()))"))
