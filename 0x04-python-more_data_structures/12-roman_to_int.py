#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string \
                    or isinstance(roman_string, int):
        return int(0)
    try:
        arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
        prev = arabic[roman_string[-1]]
        num = 0
        cur = 0
        for c in reversed(roman_string):
            cur = arabic[c]
            if (cur < prev):
                num -= cur
            else:
                num += cur
            prev = cur
        return int(num)
    except KeyError:
        return int(0)
