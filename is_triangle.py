# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/56606694ec01347ce800001b


def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False
    return False


print(is_triangle(3, 4, 5))
