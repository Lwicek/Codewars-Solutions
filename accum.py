# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039


def accum(s):
    ret_ = ""
    for c in range(len(s)):
        for i in range(1, c + 2):
            if i == 1:
                ret_ += s[c].upper()
            else:
                ret_ += s[c].lower()
        if c != len(s) - 1:
            ret_ += '-'
    return ret_


print(accum("abcd"))
