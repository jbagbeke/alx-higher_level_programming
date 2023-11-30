#!/bin/bash
# Displays the body of the response
if [[ $(curl -w "%{http_code}" -s -o /dev/null $1) -eq 200 ]]; then curl $1; fi
