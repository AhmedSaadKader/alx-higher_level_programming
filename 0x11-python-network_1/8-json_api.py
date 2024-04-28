#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={"q": q})
    res = r.json()
    if not r:
        print('No result')
    else:
        print('[{}] {}'.format(res['id'], res['name']))
