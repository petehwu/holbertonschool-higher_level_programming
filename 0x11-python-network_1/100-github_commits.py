#!/usr/bin/python3
"""This script gets commits from github"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    header = {"Accept": "application/vnd.github.v3+json"}
    res = requests.get(url, headers=header)
    res_dict = res.json()
    ele = []
    num = 0
    runner = 0
    for d in res_dict:
        if d.get("commit").get("author").get("date") ==\
           d.get("commit").get("committer").get("date"):
            ele.append(d)
            num += 1
        if num == 10:
            break
    for x in ele:
        print("{}: {}".format(x.get("sha"),
                              x.get("commit").get("author").get("name")))
