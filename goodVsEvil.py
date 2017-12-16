# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/52761ee4cffbc69732000738


def goodVsEvil(good, evil):
    goodside = [1, 2, 3, 3, 4, 10]
    badside = [1, 2, 2, 2, 3, 5, 10]

    worth_g = 0
    worth_e = 0
    g = good.split(' ')
    e = evil.split(' ')

    for i in range(len(g)):
        worth_g += goodside[i] * int(g[i])
    for o in range(len(e)):
        worth_e += badside[o] * int(e[o])

    if worth_g > worth_e:
        return "Battle Result: Good triumphs over Evil"
    elif worth_e > worth_g:
        return "Battle Result: Evil eradicates all trace of Good"
    elif worth_g == worth_e:
        return "Battle Result: No victor on this battle field"


print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
