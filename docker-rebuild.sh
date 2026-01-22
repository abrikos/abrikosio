#!/bin/bash
BASEDIR=$(dirname "$0")
cd "$BASEDIR" || exit
GIT=$(git pull 2>&1 | head -n 1)

if [[ $GIT =~ Already up to date. ]]; then
  echo "$GIT"
  date > "$BASEDIR/updated.txt"
fi
