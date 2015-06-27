__author__ = 'PyBeaner'
import time


def timeit(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Elapsed:%.10f seconds on Function(%s)" % (end - start,func.__name__))
        return result

    return wrap


@timeit
def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i

    return the_sum

@timeit
def sum_of_n_3(n):
    return n * (n + 1) / 2


if __name__ == '__main__':
    sum_of_n(10000000)
    sum_of_n_3(10000000)
