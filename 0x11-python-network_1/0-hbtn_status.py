#!/usr/bin/python3
"""Fetches url and displays the response."""
import urllib.request

if __name__ == "__main__":
    # create a request object for the URL
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    # use a with statement to open the URL
    with urllib.request.urlopen(request) as response:
        # read the response body
        body = response.read().decode('utf-8')
        # display the response in the required format
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
