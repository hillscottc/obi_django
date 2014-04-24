#!/bin/bash
# Create a new user and database for a project
# https://raw.githubusercontent.com/fiee/generic_django_project/master/tools/makeuser.sh

USER=$1
PASS=$2
#WEBDIR=/var/www
USCRIPT=userscript.sql;

if [ "${PASS}" == "" ]; then
  echo "Missing parameter!"
  echo "Usage: $0 username password"
  exit 1
fi


##  DO WITH VIRTUALENVWRAPPER
#echo "
#cd /var/www/${USER} && source bin/activate
#" >> /home/${USER}/.profile

#echo "Creating website directory ${WEBDIR}/${USER}"
## already in fabfile
#mkdir "${WEBDIR}/${USER}"
#chown -R "${USER}:${USER}" "${WEBDIR}/${USER}"
#echo "Creating symlink in user's home"
## already in fabfile
#ln -s "${WEBDIR}/${USER}" "/home/${USER}/www"
#chown -R "${USER}:${USER}" "/home/${USER}"


echo "
create role ${USER} WITH CREATEDB LOGIN PASSWORD '${PASS}';
create database ${USER}_db WITH OWNER ${USER} ENCODING 'UTF8';
" > ${USCRIPT}


echo "Setting up ${USER} in postgres...."
sudo -u postgres psql < ${USCRIPT}
rm ${USCRIPT}