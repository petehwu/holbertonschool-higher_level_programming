#!/usr/bin/python3
"""this script will allow user to search twitter"""
import requests
import base64
import sys

if __name__ == "__main__":
    # k1 = '1x1QdHz9GmTWNVrJ7F8H6F49X'
    # k2 = 'QrbOB84Qorunk0AlQSj7a2vpFZaIiWYEc0stXhYBdTI7bDvQxZ'
    # token = '{}:{}'.format(k1, k2).encode('ascii')
    token = '{}:{}'.format(sys.argv[1], sys.argv[2]).encode('ascii')
    ks = base64.b64encode(token)
    ks = ks.decode('ascii')
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    auth_headers = {
            'Authorization': 'Basic {}'.format(ks),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            }
    auth_data = {
            'grant_type': 'client_credentials'
            }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json().get('access_token')
    search_headers = {
            'Authorization': 'Bearer {}'.format(access_token)
            }
    search_params = {
            'q': sys.argv[3],
            'result_type': "recent",
            'count': 5
            }
    search_resp = requests.get(search_url,
                               headers=search_headers, params=search_params)
    for x in search_resp.json().get('statuses'):
        print("[{}] {} by {}".format(x.get('id'), x.get('text'),
                                     x.get('user').get('name')))
