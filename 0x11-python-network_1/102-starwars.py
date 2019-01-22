#!/usr/bin/python3
""" This script will do a lookup on the starwars lookup using requests
package"""
import requests
import sys

if __name__ == "__main__":
    url = "https://swapi.co/api/people/"
    if len(sys.argv) == 1:
        val = ""
    else:
        val = sys.argv[1]
    res = requests.get(url, params={"search": val})
    tot = res.json().get('count')
    res_dict = res.json()
    added = 0
    page = 1
    print("Number of results: {}".format(tot))
    while added < tot:
        for i in res_dict.get('results'):
            added += 1
            print(i.get('name'))
            for x in i.get('films'):
                req = requests.get(x)
                print("\t {}".format(req.json().get("title")))
        page += 1
        res = requests.get(url, params={"search": val, "page": page})
        res_dict = res.json()
