#!/bin/bash
#script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -sXH POST "Content-Type: application/json" "$1" -d @"$2"
