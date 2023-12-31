#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nbr_elements = 0
    for n in range(x):
        try:
            if type(my_list[n]) is int:
                print("{:d}".format(my_list[n]), end="")
                nbr_elements += 1
        except (ValueError):
            pass
    print("")
    return (nbr_elements)
