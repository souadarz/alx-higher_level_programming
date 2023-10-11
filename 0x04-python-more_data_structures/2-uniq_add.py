#!/usr/bin/python3
def uniq_add(my_list=[]):
    li_st = set(my_list)
    result = 0
    for n in li_st:
        result += n
    return (result)
