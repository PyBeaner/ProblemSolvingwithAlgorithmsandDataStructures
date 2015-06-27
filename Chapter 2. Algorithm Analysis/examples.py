__author__ = 'PyBeaner'
import time


def timeit(func):
    def wrap(*args, **kwargs):
        print("Starts to run function:", func.__name__)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Finished the function:", func.__name__)
        print("Elapsed:%.6f seconds" % (end - start))
        return result

    return wrap


@timeit
def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i

    return the_sum


if __name__ == '__main__':
    print(sum_of_n(10000))
