#!/usr/bin/python3
"""this script gets the userid for username/pwd combo from github"""
import requests
import sys
if __name__ == "__main__":
    url = "https://api.github.com/user"
    header = {"Accept": "application/vnd.github.v3+json"}
    res = requests.get(url, headers=header, auth=requests.auth.
                       HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    res_dict = res.json()
    print(res_dict.get('id'))
