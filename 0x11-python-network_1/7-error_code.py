#!/usr/bin/python3
""" Sends a request to URL and displays body of the response """
import requests
import sys

if __name__ == '__main__':
    try:
        http_res = requests.get(sys.argv[1])
        http_res.raise_for_status()
        print(http_res.text)
    except requests.exceptions.HTTPError:
        if http_res.status_code >= 400:
            print('Error code: {}'.format(http_res.status_code))
