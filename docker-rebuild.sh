#!/bin/bash
BASEDIR=$(dirname "$0")
cd "$BASEDIR" || exit
GIT=$(git pull 2>&1 | head -n 1)
echo "$GIT"
if [[ $GIT =~ Из ]]; then
  date > "$BASEDIR/updated.txt"
fi
