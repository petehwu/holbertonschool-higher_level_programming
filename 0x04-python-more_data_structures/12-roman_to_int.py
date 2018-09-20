#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return int(0)
    try:
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        arabic = [1, 5, 10, 50, 100, 500, 1000]
        prev = arabic[roman.index(roman_string[-1])]
        num = 0
        cur = 0
        for c in reversed(roman_string):
            cur = arabic[roman.index(c)]
            if (cur < prev):
                num -= cur
            else:
                num += cur
            prev = cur
        return int(num)
    except ValueError:
        return int(0)
