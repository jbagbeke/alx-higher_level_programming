#!/usr/bin/python3
""" Sends request to URL and displays value of var X-Request-Id """
import requests

if __name__ == '__main__':
    http_res = requests.get('https://alx-intranet.hbtn.io/status')

    print(http_res.headers['X-Request-Id'])
