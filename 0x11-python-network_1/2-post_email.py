#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
import sys
import urllib.request


if __name__ == '__main__':
    email = sys.argv[2]
    value = {"email": email}
    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
