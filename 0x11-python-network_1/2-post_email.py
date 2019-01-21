#!/usr/bin/python3
"""This script sends a POST command and sends an e-mail address"""
import urllib.request
import urllib.parse
import sys

val = {"email": sys.argv[2]}
data = urllib.parse.urlencode(val)
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
if __name__ == "__main__":
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print("{}".format(html.decode("utf-8")))
