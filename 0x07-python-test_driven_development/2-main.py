#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
print ("--")
matrix = [
    [1, 2, 3,  4],
    [2, 5, 6, 9]
]
print(matrix_divided(matrix, 3))
print(matrix)
print ("--")
matrix = [
    [1, 2, 6],
    [4, 5, 6],
    [3, 6, 8]
]
print(matrix_divided(matrix, 3))
print(matrix)
print ("--")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix = []
print(matrix_divided(matrix, 5))
print(matrix)
