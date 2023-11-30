#!/bin/bash
# Displays the size of the body of the response

request=$(curl -I -s $1)

length=$(echo "$request" | grep -i 'Content-Length' | awk '{print $2}')

echo "$length"
