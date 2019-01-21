#!/usr/bin/python3
"""This script fetches a URL"""
import requests
import sys

if __name__ == "__main__":
    try:
        html = requests.get(sys.argv[1])
        html.raise_for_status()
        print("{}".format(html.text))
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(html.status_code))
