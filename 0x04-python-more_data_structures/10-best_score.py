#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    scores = list(a_dictionary.values())
    scores.sort(reverse=True)
    best = scores[0]
    for name, score in a_dictionary.items():
        if score == best:
            return name
