#!/usr/bin/python3
"""
 Python script that takes a URL as input, sends a request to the
 URL, and displays the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])
    # check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
