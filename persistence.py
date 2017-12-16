# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec


def persistence(n):
    steps = 0
    if 10 > n:
        return steps
    while True:
        str_ = str(n)
        s_ = int(str(n)[0])
        for c in range(1, len(str_)):
            s_ *= int(str_[c])
        steps += 1
        if 10 > s_:
            return steps
        else:
            n = s_


print(persistence(999))
