#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for n, m in sorted(a_dictionary.items()):
        print("{}: {}".format(n, m))
