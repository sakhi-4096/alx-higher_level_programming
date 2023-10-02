#!/usr/bin/python3
"""
Python script that takes a letter as input, sends a POST request
to the specified URL with the letter as a parameter, and processes
the response according to the specified criteria.
"""
from sys import argv
import requests


if __name__ == "__main__":
    # get the letter from the command-line argument, default to empty
    # string if not provided
    letter = argv[1] if len(argv) > 1 else ""

    # create a dictionary with the letter as a parameter
    data = {'q': letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    # check if the response has a valid JSON format and is not empty
    if (response.headers.get('content-type') == 'application/json' and
            response.text.strip()):
        # check if 'id' and 'name' keys are present in the JSON
        if 'id' in json_data and 'name' in json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")

    else:
        print("Not a valid JSON")
