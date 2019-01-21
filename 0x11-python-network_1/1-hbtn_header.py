#!/usr/bin/python3
"""This script fetches a URL"""
import urllib.request
from sys import argv
with urllib.request.urlopen(argv[1]) as response:
    header = response.info()
print(header['X-Request-Id'])
