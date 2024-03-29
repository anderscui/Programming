#!/bin/bash

FILE=/etc/passwd

read -p "enter a user name:" user_name

file_info="$(grep "^$user_name:" $FILE)"

if [ -n "$file_info" ]; then
  IFS=":"
  read user pw uid gid name home shell <<< "$file_info"
  echo "User = '$user'"
  echo "Shell = '$shell'"
else
  echo "No such user '$user_name'" >&2
  exit 1
fi
