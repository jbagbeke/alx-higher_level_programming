#!/usr/bin/python3
""" Sends request to URL and displays value of X-Request-Id var """
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as url:
        print(url.headers.get('X-Request-Id'))
