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


if __name__ == '__main__':
    print(solution1("abcd", "dcba"))
    print(solution2("abcd", "dcba"))
