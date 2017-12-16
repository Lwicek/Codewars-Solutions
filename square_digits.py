# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/546e2562b03326a88e000020


def square_digits(num):
    ret = ""
    num = str(num)
    for n in num:
        n_ = pow(int(n), 2)
        ret += str(n_)
    return int(ret)


print(square_digits(10))
