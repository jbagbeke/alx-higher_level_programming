#!/usr/bin/python3
""" Sends POST request to passed URL with the email as parameter """
import requests
import sys

if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    http_res = requests.post(sys.argv[1], data=email)

    if http_res.status_code == 200:
        print(http_res.text())
