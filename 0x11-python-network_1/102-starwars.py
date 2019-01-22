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
    res_dict = res.json()
    tot = res_dict.get("count")
    print("Number of results: {}".format(tot))
    while res_dict:
        for i in res_dict.get('results'):
            print(i.get('name'))
            for x in i.get('films'):
                req = requests.get(x)
                print("\t {}".format(req.json().get("title")))
        if (res_dict.get('next')):
            res = requests.get(res_dict.get("next"))
            res_dict = res.json()
        else:
            res_dict = None
