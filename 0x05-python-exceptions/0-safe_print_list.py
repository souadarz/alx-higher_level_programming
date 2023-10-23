#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbr_elements = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            nbr_elements += 1
        except:
            break
    print("")
    return (nbr_elements)
