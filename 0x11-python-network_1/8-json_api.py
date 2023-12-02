#!/usr/bin/python3
""" Sends a POST request to url with the letter as a parameter """
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    let = {'q': q}
    http_res = requests.post('http://0.0.0.0:5000/search_user', data=let)
    
    try:
        http_json = http_res.json()

        if not http_json:
            print('No result')
        else:
            print('[{}] {}'.format(http_json['id'], http_json['name']))
    except:
        print('Not a valid JSON')
