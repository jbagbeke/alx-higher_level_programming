#!/bin/bash
# Displays the body of the response
if [[ $(curl -I -s $1 | grep -i 'HTTP/1.1' | awk '{print $2}') -eq 200 ]]; then curl -s $1; fi
