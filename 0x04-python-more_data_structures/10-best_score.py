#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
            return None
    return (sorted(a_dictionary.items(), key = lambda kg: (kg[1], kg[0]))[-1][0])
