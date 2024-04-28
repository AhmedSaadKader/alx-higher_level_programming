#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(r.headers.get('X-Request-Id'))