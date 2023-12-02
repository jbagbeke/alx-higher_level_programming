#!/usr/bin/python3
""" Takes GitHub credentials and uses GitHub API to display id """
import requests
import sys

if __name__ == '__main__':
    git_url = "https://api.github.com/user"
    git_head = {'Authorization': 'token {}'.format(sys.argv[2])}

    http_res = requests.get(git_url, headers=git_head)

    try:
        http_json = http_res.json()

        http_res.raise_for_status()

        if not http_json:
            print(None)

        print(http_json.get('id'))
    except requests.exceptions.HTTPError as e:
        print(None)
    except requests.exceptions.RequestException as e:
        print(None)
