#!/usr/bin/python3
""" Sends POST request to passed URL with the email as parameter """
import requests
import sys

if __name__ == '__main__':
    email = sys.argv[2]
    http_res = requests.post(sys.argv[1], data=email)

    if http_res:
        print(http_res.text())
