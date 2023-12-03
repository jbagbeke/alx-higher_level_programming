#!/bin/bash
# Makes request to server respond with a message containing You got me!
curl -s "0.0.0.0:5000/catch_me" -w "You got me!" -o /dev/null
