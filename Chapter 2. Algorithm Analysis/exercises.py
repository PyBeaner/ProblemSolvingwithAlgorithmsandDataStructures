import random

__author__ = 'PyBeaner'
import timeit
#
# # 1. Devise an experiment to verify that the list index operator is O(1).
li = []
pos = 0
for i in range(100000, 1000001, 100000):
    li = list(range(i))
    pos = random.randrange(i)
    t = timeit.Timer("li[pos]", "from __main__ import li,pos")
    print("%d,%10.3f" % (i, t.timeit()))
#
# # 2. Devise an experiment to verify that get item and set item are ?(1) for dictionaries.
d = {}
key = 0
for i in range(100000, 1000001, 100000):
    d = {j: None for j in range(i)}
    key = random.randrange(i)
    t = timeit.Timer("key in d", "from __main__ import d,key")
    print("%d,%10.3f" % (i, t.timeit()))

# # 3. Devise an experiment that compares the performance of the del operator on lists and
# dictionaries.
for i in range(1000000, 10000001, 1000000):
    d = {j: None for j in range(i)}
    li = list(range(i))
    pos = key = random.randrange(i)
    t1 = timeit.Timer("del d[key]", "from __main__ import d,key")
    t2 = timeit.Timer("del li[pos]", "from __main__ import li,pos")
    print("%d,%10.3f,%10.3f" % (i, t1.timeit(1), t2.timeit(1)))


# # 4. Given a list of numbers in random order write a linear time algorithm to find the kth
# smallest number in the list. Explain why your algorithm is linear.

def smallest_k(the_list, k):
    # sort the list
    counts = {}
    # O(n)
    for i in range(len(the_list)):
        ele = the_list[i]
        counts.setdefault(ele, 0)
        counts[ele] += 1
    return_list = []
    # len(counts)
    for key in counts:
        count = counts[key]
        take = min(k, count)
        return_list += [key] * take
        k -= take
        if k <= 0:
            break
    return return_list

k = 1
li = []
for i in range(100, 1001, 100):
    li = [random.randint(0, j) for j in range(i)]
    k = 10
    t = timeit.Timer("smallest_k(li,k)", "from __main__ import smallest_k,li,k")
    print("{:.10f} finding the smallest {} items in len={} list :".format(t.timeit(1), k, i))
