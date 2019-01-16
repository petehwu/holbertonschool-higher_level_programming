#!/bin/bash
#this script shows only the response code
curl -o /dev/null -s -w "%{http_code}" "$1"
