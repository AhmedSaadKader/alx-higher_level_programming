#!/usr/bin/python3
"""Takes your github credentials (username and password) and uses the
github api to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    r = requests.get('https://api.github.com/user', auth=auth)
    print(r.json().get("id"))
