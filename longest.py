# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/5656b6906de340bd1b0000ac


def longest(s1, s2):
    alb = "abcdefghijklmnopqrstuvwxyz"
    ret = ""
    for i in s1:
        if i in alb and i not in ret:
            ret += i
    for l in s2:
        if l in alb and l not in ret:
            ret += l
    return ''.join(sorted(ret))


print("Roman", "Masar")
