#!/usr/bin/python3
""" Script that takes 2 arguments in order to solve this challenge """
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"
    git_url = url.format(sys.argv[2], sys.argv[1])

    http_res = requests.get(git_url)

    try:
        http_json = http_res.json()

        http_res.raise_for_status()

        if not http_json:
            print(None)

        for commit in http_json:
            print("{}: {}".format(commit.get('sha'),
                                  commit.get('commit')['author']['name']))
    except requests.exceptions.HTTPError as e:
        print(None)
    except requests.exceptions.RequestException as e:
        print(None)
