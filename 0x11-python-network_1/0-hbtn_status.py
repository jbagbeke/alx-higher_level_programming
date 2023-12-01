#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as url:

    content = url.read()
    print("""Body response:
    \t- type: {}
    \t- content: {}
    \t- utf8 content: {}""".format(type(content),
                                   content,
                                   content.decode('utf-8')))
