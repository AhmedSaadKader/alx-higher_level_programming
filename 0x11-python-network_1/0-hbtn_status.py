#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        re = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(re)))
        print("\t- content: {}".format(re))
        print("\t- utf8 content: {}".format(re.decode('utf-8')))
