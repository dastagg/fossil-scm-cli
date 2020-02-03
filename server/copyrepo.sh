#!/bin/bash
# run as sudo!

if [ -z "$1" ]; then
  echo usage: $0 repository
  exit
fi
REPO=$1

mv ../upload/$REPO.fsl /var/www/fossils/

chown www-data:www-data /var/www/fossils/$REPO.fsl
