#!/bin/bash
# Sends JSON POST request to URL and displays body of response
curl -X POST -H "Content-Type: application/json" -d "$(cat "$2")" $1
