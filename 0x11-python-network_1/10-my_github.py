#!/usr/bin/python3
"""
Python script that takes your GitHub username and personal access
token as arguments and uses Basic Authentication to access the GitHub
API and display your user ID:
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # define the GitHub API endpoint for user information
    api_url = "https://api.github.com/user"

    # set up Basic Authentication with your username and personal access token
    # send a GET request to the GitHub API with Basic Authentication
    response = requests.get(api_url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(response.json().get('id'))
