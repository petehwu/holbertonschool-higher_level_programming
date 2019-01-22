#!/usr/bin/python3
"""This script gets commits from github"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                              sys.argv[2])
    res = requests.get(url)
    res_dict = res.json()
    for d in res_dict[:10]:
        print("{}: {} {}".format(d.get("sha"), d["commit"]["author"]["name"]))
