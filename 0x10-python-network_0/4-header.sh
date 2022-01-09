#!/bin/bash
#script that takes in a URL as an argument, sends a GET request to the URL,and displays the body of the response.
curl "$1" -sHX GET "X-School-User-Id:98"
