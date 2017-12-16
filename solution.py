# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/51675d17e0c1bed195000001


def solution(digits):
    temp = 0
    for i in range(len(digits)):
        if int(digits[i:i + 5]) > temp:
            temp = int(digits[i:i + 5])
    return temp


print(solution(1234567890))
