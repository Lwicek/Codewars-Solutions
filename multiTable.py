# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce


def multiTable(number):
    ret = ""
    for i in range(1, 11):
        mat_ = i * number
        if i < 10:
            ret += str(i) + " * " + str(number) + " = " + str(mat_) + '\n'
        elif i == 10:
            ret += str(i) + " * " + str(number) + " = " + str(mat_)
    return ret


print(multiTable(3))
