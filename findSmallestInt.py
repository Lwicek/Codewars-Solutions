# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/55a2d7ebe362935a210000b2


def findSmallestInt(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest


print(findSmallestInt([1, 2, 3, 4, 5]))
