#!/bin/bash
# This is

if [ -z "$1" ]; then
  echo usage: $0 repository
  exit
fi
REPO=$1
FOSHOME="$HOME/dev/FOSSIL"
FOSIGNORE="$HOME/dev/FOSSIL/.fossil-settings"
FOSFILES="$HOME/dev/FOSSIL/fossil-files"

fossil init $FOSHOME/$REPO.fsl
fossil config import $FOSFILES/ticket.config -R $FOSHOME/$REPO.fsl

fossil open $FOSHOME/$REPO.fsl

cp -r $FOSIGNORE .
