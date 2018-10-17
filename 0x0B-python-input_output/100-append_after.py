#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    fileList = []

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    with open(filename, mode="r", encoding="utf-8") as readFile:
        for line in readFile:
            fileList.append(line)
            if search_string in line:
                fileList.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as writeFile:
        for l in fileList:
            writeFile.write(str(l))
