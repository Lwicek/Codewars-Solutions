# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155


def Descending_Order(num):
    if num > -1:
        num = str(num)
        num = sorted(num)
        num = ''.join(reversed(num))
        return int(num)


print(Descending_Order(10))
