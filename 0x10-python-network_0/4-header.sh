#!/bin/bash
# add header variable, displays "Hello School!", Usage: ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
curl -sH "X-School-User-Id: 98" "$1"
