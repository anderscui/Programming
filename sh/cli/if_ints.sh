#!/bin/bash

INT=-5

if [ -z "$INT" ]; then
  echo "INT is empty." >&2
  exit 1
fi

if [ "$INT" -eq 0 ]; then
  echo "zero value"
else
  if [ "$INT" -lt 0 ]; then
    echo "INT negative"
  else
    echo "INT is positive"
  fi

  if [ $((INT % 2)) -eq 0 ]; then
    echo "INT is even"
  else
    echo "INT is odd"
  fi
fi

exit
