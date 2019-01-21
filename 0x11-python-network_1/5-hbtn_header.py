#!/usr/bin/python3
"""This script fetches a URL"""
import requests
import sys

if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    print("{}".format(html.headers['X-Request-Id']))
