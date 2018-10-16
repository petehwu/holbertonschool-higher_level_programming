#!/usr/bin/python3
read_lines = __import__('2-read_lines').read_lines

print("1 line:")
read_lines("my_file_0.txt", 1)
print("--")
print("3 lines:")
read_lines("my_file_0.txt", 3)
print("--")
print("Full content, line_number = 0:")
read_lines("my_file_0.txt")
print("--")
print("Full content, line_number = -1:")
read_lines("my_file_0.txt", -1)
print("--")
print("Full content, line_number = 50:")
read_lines("my_file_0.txt", 50)

