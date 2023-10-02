#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py [letter only]
"""
from sys import argv
import requests

if __name__ == "__main__":
    search_letter = argv[1] if len(argv) > 1 else ""
    search_url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': search_letter}
    response = requests.post(search_url, data=payload)

    try:
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json.get(
                'id'), response_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
