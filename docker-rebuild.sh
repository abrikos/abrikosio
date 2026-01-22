#!/bin/bash
BASEDIR=$(dirname "$0")
cd "$BASEDIR" || exit
GIT=$(git pull 2>&1 | head -n 1)

if [[ $GIT =~ Already ]]; then
  echo "$GIT"
else
  echo "$GIT"
  date > "$BASEDIR/updated.txt"
  echo "Changes"
fi

