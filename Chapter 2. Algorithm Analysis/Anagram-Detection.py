__author__ = 'PyBeaner'
# For example, 'heart' and 'earth' are anagrams


# O(n2)
def solution1(s1, s2):
    anagram = True
    for c in s1:
        if c in s2:
            continue
        else:
            anagram = False
            break
    return anagram


# O(n2) or O(nlogn)
def solution2(s1, s2):
    # nlog(n) or n2
    s1 = sorted(s1)
    s2 = sorted(s2)
    # n
    return s1 == s2


# O(n)
def solution3(s1, s2):
    counter1 = {}
    counter2 = {}
    # O(n)
    for c in s1:
        counter1.setdefault(c, 0)
        counter1[c] += 1
    # O(n)
    for c in s2:
        counter2.setdefault(c, 0)
        counter2[c] += 1
    for c in counter1:
        # O(n)*1
        if c not in counter2:
            return False
        # O(n)*1
        if counter1[c] != counter2[c]:
            return False
    return True


if __name__ == '__main__':
    print(solution1("abcd", "dcba"))
    print(solution2("abcd", "dcba"))
    print(solution3("bdcd", "dcbd"))
