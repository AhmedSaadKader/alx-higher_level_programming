#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))