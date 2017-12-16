# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/563b662a59afc2b5120000c6


def nb_year(p0, percent, aug, p):
    for i in range(1, 1000):
        if p0 + p0 * (percent / 100) + aug >= p:
            return i
        else:
            p0 = p0 + p0 * (percent / 100) + aug


print(1000, 3, 200, 5000)
