#!/bin/bash

FILE=~/.bashrc

if [ -e "$FILE" ]; then
  if [ -f "$FILE" ]; then
    echo "$FILE is a regular file"
  fi
  if [ -r "$FILE" ]; then
    echo "$FILE is readable"
  fi
  if [ -x "$FILE" ]; then
    echo "$FILE is executable/searchable"
  fi
else
  echo "$FILE does not exist"
fi

exit
