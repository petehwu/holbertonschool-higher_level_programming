#!/usr/bin/python3

from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
tlist = []
try:
    tlist = load_from_json_file(filename)
except:
    pass
for i in range(1, len(argv)):
    tlist.append(argv[i])
save_to_json_file(tlist, filename)
