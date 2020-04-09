#!/bin/bash
# Task 03
curl $1 | grep Allow | cut  -d ':' -f 2 | sed -e 's/^[[:space:]]*//'
