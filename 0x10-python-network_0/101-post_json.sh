#!/bin/bash
#this script posts a json file using curl
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
