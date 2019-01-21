#!/usr/bin/python3
"""This script display the X-Request-Id from the header of response """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
