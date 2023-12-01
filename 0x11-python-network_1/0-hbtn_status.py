#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

with urllib.request.urlopen(request) as url:

    content = url.read()
    print("""Body response:
    \t- type: {}
    \t- content: {}
    \t- utf8 content: {}""".format(type(content),
                                   content,
                                   content.decode('utf-8')))
