#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        tup_le = (len(sentence), sentence[0])
    else:
        tup_le = (len(sentence), None)
    return (tup_le)
