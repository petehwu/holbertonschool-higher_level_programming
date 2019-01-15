#!/bin/bash
# This script shows only Allowed methods for server
curl -ILs "$1" | grep "Allow: " | cut -d" " -f2,3,4
