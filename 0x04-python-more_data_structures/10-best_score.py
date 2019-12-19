#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return (sorted(a_dictionary.items(), key = lambda k : (k[1], k[0]))[-1][0])
