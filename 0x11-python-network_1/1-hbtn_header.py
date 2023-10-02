#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        # print the value of the 'X-Request-Id' header if it exists
        print(dict(response.headers).get("X-Request-Id"))
