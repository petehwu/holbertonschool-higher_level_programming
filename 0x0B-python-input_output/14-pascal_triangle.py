#!/usr/bin/python3

def pascal_triangle(n):
    """prints out a pascal's triangle"""
    bigList = []
    rowList = []
    prevRow = []
    for row in range(n):
        rowList = []
        for col in range(row + 1):
            if col == 0:
                rowList.append(1)
            else:
                val1 = prevRow[col - 1]
                if col == len(prevRow):
                    val2 = 0
                else:
                    val2 = prevRow[col]
                tot = val1 + val2
                rowList.append(tot)
        prevRow = list(rowList)
        bigList.append(rowList)
    return (bigList)
