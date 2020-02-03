#!/bin/bash

shopt -s nullglob
for f in *.fsl
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  fossil rebuild $f
  echo "Fossil rebuild run on: " $f
done
