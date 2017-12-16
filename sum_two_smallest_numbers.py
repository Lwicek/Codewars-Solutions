# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/558fc85d8fd1938afb000014


def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]


print(sum_two_smallest_numbers([5, 8, 13, 20, 15, 4]))
