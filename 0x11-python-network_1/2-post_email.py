#!/usr/bin/python3
"""This script sends a POST command and sends an e-mail address"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
