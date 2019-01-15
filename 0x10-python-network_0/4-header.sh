#!/bin/bash
# This script sends a GET with a Header variable
curl -sL "$1" -X GET -H "X-HolbertonSchool-User_Id: 98"
