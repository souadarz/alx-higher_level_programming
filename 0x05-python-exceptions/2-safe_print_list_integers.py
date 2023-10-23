#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nbr_elements = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            nbr_elements += 1
        except (IndexError, ValueError):
            pass
    print("")
    return (nbr_elements)
