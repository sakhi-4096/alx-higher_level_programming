#!/usr/bin/python3
"""
Python script that takes a URL and an email address as input,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    # Get the URL and email from the command-line arguments
    url = argv[1]
    # Create a dictionary with the email as a parameter
    data = {'email': argv[2]}

    response = requests.post(url, data=data)
    # Display the body of the response
    print(response.text)
