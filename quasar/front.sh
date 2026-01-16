#!/bin/bash
echo "static for Django"
#rm -fr ../static/quasar/*;
cp -r ../blog/templates/* ../static/
git add ../blog/templates/index.html
git add ../static/*
ls -l ../static/