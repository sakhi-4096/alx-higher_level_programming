#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)

    commits = response.json()
    for i, commit in enumerate(commits[:10], start=1):
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(f"Commit {i}: {sha} by {author}")
