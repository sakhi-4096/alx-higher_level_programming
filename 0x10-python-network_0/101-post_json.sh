#!/bin/bash
# post contents of file
# Usage: ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""

curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"