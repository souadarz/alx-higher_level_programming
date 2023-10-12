#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for n, m in a_dictionary.items():
            if m is max(a_dictionary.values()):
                return (n)
    else:
        return (None)
