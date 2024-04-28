#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
import sys
import requests


if __name__ == '__main__':
    email = sys.argv[2]
    value = {"email": email}
    r = requests.post(sys.argv[1], value)
    print(r.text)
