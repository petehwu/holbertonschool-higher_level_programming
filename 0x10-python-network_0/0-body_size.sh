#!/bin/bash
# This script sends request to URL and display sie of the body
curl -Is  "$1" | grep "Content-Length:" | cut -d" " -f2
