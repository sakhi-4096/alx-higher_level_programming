#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response
(decoded in utf-8). Handles HTTPError exceptions and prints the
HTTP status code in case of an error.
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    # get the URL from the command-line argument
    url = sys.argv[1]

    try:
        # create a request object for the URL
        request = urllib.request.Request(url)
        # use a with statement to open the URL
        with urllib.request.urlopen(request) as response:
            # read and decode the response in UTF-8
            body = response.read().decode('utf-8')
            # display the decoded response body
            print(body)

    except urllib.error.HTTPError as e:
        # handle HTTPError exceptions and print the HTTP status code
        print("Error code: {}".format(e.code))
