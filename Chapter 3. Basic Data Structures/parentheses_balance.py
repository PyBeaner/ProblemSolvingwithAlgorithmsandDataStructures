__author__ = 'PyBeaner'
from stack import Stack


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    for char in symbol_string:
        if char in "([{":
            s.push(char)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                left_char = s.pop()
                if not parentheses_matches(left_char, char):
                    balanced = False
                    break

    return balanced and s.is_empty()


def parentheses_matches(left, right):
    opens = "({["
    closes = ")}]"
    return opens.find(left) == closes.find(right)


print(par_checker("(((())))"))
print(par_checker("(((()))"))
print(par_checker("(()))"))

print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
