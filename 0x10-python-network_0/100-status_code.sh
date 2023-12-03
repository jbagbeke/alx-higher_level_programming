#!/bin/bash
# Sends request to a URL and displays status code of the response
curl -I -s -w '%{http_code}\n' $1 -o /dev/null
