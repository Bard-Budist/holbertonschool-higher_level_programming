#!/bin/bash
# Task 00
curl -sI $1 | grep "Content-Length" | awk '{print $2}'
