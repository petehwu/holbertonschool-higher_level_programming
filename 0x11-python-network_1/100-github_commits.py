#!/usr/bin/python3
"""This script gets commits from github"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    ds = {"since": "since=2019-01-18T00:00:00Z"}
    header = {"Accept": "application/vnd.github.v3+json"}
    res = requests.get(url, headers=header, params=ds)
    res_dict = res.json()
    for d in res_dict[:10]:
        print("{}: {}".format(d.get("sha"),
                              d.get("commit").get("author").get("name")))
