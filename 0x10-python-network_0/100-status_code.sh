#!/bin/bash
# Task 06
curl -s -o /dev/null -w "%{http_code}" $1
