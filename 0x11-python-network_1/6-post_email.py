#!/usr/bin/python3
"""This script fetches a URL"""
import requests
import sys

if __name__ == "__main__":
    html = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(html.text))
