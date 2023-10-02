#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the response body.
Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # create a dictionary with the email as a parameter
    data = urllib.parse.urlencode({'email': email}).encode("ascii")

    # create a POST request with the data
    request = urllib.request.Request(url, data)
    # send the POST request and retrieve the response
    with urllib.request.urlopen(request) as response:
        # read and decode the response in UTF-8
        body = response.read().decode('utf-8')
        print(body)
