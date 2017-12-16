# By Roman Masar 14.12.2017
# https://www.codewars.com/kata/550554fd08b86f84fe000a58


def in_array(array1, array2):
    ret_ = []
    for i in array1:
        for o in array2:
            if i in o:
                if i not in ret_:
                    ret_.append(i)
    return sorted(ret_)


print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
