__author__ = 'PyBeaner'


# Implement the Stack ADT
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # O(1)
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) <= 0

    def pop(self):
        # O(1)
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def size(self):
        return len(self)

    def __str__(self):
        return str(self.items)


class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        # O(N)
        self.items.insert(0, item)

    def pop(self):
        # O(N)
        self.items.pop(0)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(10)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
