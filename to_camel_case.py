# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/517abf86da9663f1d2000003


def to_camel_case(text):
    #your code here
    ret_ = ""
    for c in range(len(text)):
        if text[c] == "_" or text[c] == "-":
            continue
        if text[c-1] == "_" or text[c-1] == "-":
            ret_ += text[c].upper()
            continue
        else:
            ret_ += text[c]
            continue
    return ret_

print("_roman-masar")