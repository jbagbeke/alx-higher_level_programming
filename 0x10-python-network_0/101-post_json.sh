#!/bin/bash
# Sends JSON POST request to URL and displays body of response
curl -X POST -d $2 $1
