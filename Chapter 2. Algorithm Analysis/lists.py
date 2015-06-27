__author__ = 'PyBeaner'

import time


def timeit(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Elapsed:%.10f seconds on Function(%s)" % (end - start, func.__name__))
        return result

    return wrap


loops = 1000000


@timeit
def test1():
    l = []
    for i in range(loops):
        l += [i]


@timeit
def test2():
    l = []
    for i in range(loops):
        l.append(i)


@timeit
def test3():
    l = [i for i in range(loops)]


@timeit
def test4():
    l = list(range(loops))


if __name__ == '__main__':
    """
    Elapsed:0.2802040577 seconds on Function(test1)
    Elapsed:0.1646149158 seconds on Function(test2)
    Elapsed:0.1050739288 seconds on Function(test3)
    Elapsed:0.0465362072 seconds on Function(test4)
    """
    test1()
    test2()
    test3()
    test4()
