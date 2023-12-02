#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter """
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as url:
            print(url.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.getcode()))
    except urllib.error.URLError as e:
        print('Error code: {}'.format(e.getcode()))
    except Exception as e:
        print('Error code: {}'.format(e.getcode()))
