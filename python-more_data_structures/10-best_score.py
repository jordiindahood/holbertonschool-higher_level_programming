#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = max(a_dictionary.values())
    for ky, vl in a_dictionary.items():
        if vl == best:
            return str(ky)