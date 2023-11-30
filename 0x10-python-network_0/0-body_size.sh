#!/bin/bash
# Displays the size of the body of the response
echo "$(curl -I -s $1 | grep -i 'Content-Length' | awk '{print $2}')"
