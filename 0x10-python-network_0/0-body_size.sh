#!/bin/bash
# display size of body of the response
# ./0-body_size.sh 0.0.0.0:5000

curl -s "$1" | wc -c