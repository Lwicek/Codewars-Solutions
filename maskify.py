# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/5412509bd436bd33920011bc


def maskify(cc):
    ret = ""
    print(len(cc))
    if len(cc) > 3:
        for i in range(len(cc)):
            if i >= len(cc) - 4:
                ret += cc[i]
            else:
                ret += '#'
        return ret
    else:
        return cc


print(maskify(123456789))