#!/usr/bin/python3
""" Sends a POST request to url with the letter as a parameter """
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    http_res = requests.post('http://0.0.0.0:5000/search_user', data=q)
    content = http_res.headers.get('Content-Type', "").lower()

    if "application/json" in content:
        http_json = http_res.json()

        print('{} {}'.format(http_json['id'], http_json['name']))
    if len(content) == 0:
        print('No result')
    else:
        print('Not a valid JSON')
