#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    email = urllib.parse.urlencode({"email": sys.argv[2]}).encode('utf-8')
    
    obj = urllib.request.Request(sys.argv[1], data=email, method='POST')

    with urllib.request.urlopen(obj) as url:
        print(url.read().decode('utf-8'))
