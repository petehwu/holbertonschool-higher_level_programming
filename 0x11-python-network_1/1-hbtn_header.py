#!/usr/bin/python3
"""This script display the X-Request-Id from the header of response """
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    header = response.info()
print(header['X-Request-Id'])
