#!/bin/bash
# display status code only, Usage: ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
curl -s -o /dev/null -w "%{http_code}" "$1"
