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
    print("Number of results: {}".format(res_dict['count']))
    for i in res_dict['results']:
        print(i["name"])
