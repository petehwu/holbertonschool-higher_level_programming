#!/bin/bash
#this script posts a json file using curl
curl -X POST -H "Content-Type: application/json" -d@"$2" "$1"
