#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and displays
the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print('Error code:', e.response.status_code)
