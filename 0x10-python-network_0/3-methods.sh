#!/bin/bash
# display all methods accepted, Usage: ./3-methods.sh 0.0.0.0:5000/route_4
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
