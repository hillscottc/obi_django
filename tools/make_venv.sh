#!/bin/bash
# Create a new django virtual environment
# Requirements: virtualenvwrapper


# Verify num args not than less than 1
[ $# -lt 1 ] && { echo "Usage: $0 venv"; exit 1; }


VENV=$1

echo $VENV


#PASS=$2
#
##WEBDIR=/var/www
#USCRIPT=userscript.sql;
#
#if [ "${PASS}" == "" ]; then
#  echo "Missing parameter!"
#  echo "Usage: $0 username password"
#  exit 1
#fi
#

