#!/bin/bash
# Task 06
curl -sI $1 | grep HTTP | awk '{print $2}'
