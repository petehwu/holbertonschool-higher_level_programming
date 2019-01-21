#!/usr/bin/python3
"""This script fetches a URL"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        srch = ""
    else:
        srch = sys.argv[1]
    try:
        html = requests.post('http://34.206.234.184:41878/search_user',
                         data = {'q': srch})
        if not(html.json()):
            print ("No result")
        else:
            print("[{}] {}".format(html.json()['id'], html.json()['name']))
    except ValueError:
        print("Not a valid JSON")
    
