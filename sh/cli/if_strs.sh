#!/bin/bash

ANSWER=maybe

if [ -z "$ANSWER" ]; then
  echo "No answer found" >&2
  exit 1
fi

if [ "$ANSWER" = "yes" ]; then
  echo "The answer is YES"
elif [ "$ANSWER" = "no" ]; then
  echo "The answer is NO"
elif [ "$ANSWER" = "maybe" ]; then
  echo "The answer is MAYBE"
else
  echo "UNKNOWN answer"
fi

exit
