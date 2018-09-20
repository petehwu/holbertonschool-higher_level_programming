#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return int(0)
    try:
        roman = ['I','V','X','L','C','D','M']
        arabic = [1, 5, 10, 50, 100, 500, 1000]
        prev = arabic[roman.index(roman_string[0])]
        num = 0
        cur = 0
        for c in roman_string:
            cur = arabic[roman.index(c)]
            num += cur
            if (cur > prev):
                num -=(prev * 2)
            prev = cur
        return int(num)
    except ValueError:
        return int(0)


