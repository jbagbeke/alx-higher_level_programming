#!/usr/bin/python3
""" Sends request to URL and displays value of var X-Request-Id """
import requests
import sys

if __name__ == '__main__':
    http_res = requests.get(sys.argv[1])

    if http_res.status_code == 200:
        print(http_res.headers.get('X-Request-Id'))
