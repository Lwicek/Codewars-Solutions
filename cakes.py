# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/525c65e51bf619685c000059


def cakes(recipe, available):
    have = []
    for r in recipe:
        if r in available:
            have.append(available[r] / recipe[r])
            continue
        else:
            return 0
    have = sorted(have)
    return have[0]


print(cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}))
