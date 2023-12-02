#!/usr/bin/python3
""" Script that takes 2 arguments in order to solve this challenge """
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"
    git_url = url.format(sys.argv[2], sys.argv[1])

    http_res = requests.get(git_url)

    http_json = http_res.json()

    index = 0
    for commit in http_json:
        if (index < 10):
            print("{}: {}".format(commit.get('sha'),
                                commit['commit']['author']['name']))
        index += 1
