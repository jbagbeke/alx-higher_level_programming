#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter """
import urllib.request
import sys

if __name__ == '__main__':
    email = sys.argv[2]
    obj = urllib.request.Request(sys.argv[1], data=email, method='POST')

    with urllib.request.urlopen(obj) as url:
        print(url.read().decode('utf-8'))
