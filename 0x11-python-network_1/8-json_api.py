#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py [letter only]
"""
from sys import argv
import requests

if __name__ == "__main__":
    # check if a letter argument is provided, default to an empty string if not
    letter = argv[1] if len(argv) > 1 else ""
    # define the URL for the POST request
    search_url = 'http://0.0.0.0:5000/search_user'
    # create a payload dictionary with the letter
    request_payload = {'q': letter}
    # send the POST request
    response = requests.post(search_url, data=request_payload)

    try:
        # parse the JSON response
        response_data = response.json()

        if response_data:
            # display user information if available
            user_id = response_data.get('id')
            user_name = response_data.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            # display "No result" if no user information is available
            print("No result")
    except ValueError:
        # display "Not a valid JSON" for JSON parsing errors
        print("Not a valid JSON")
