#!/bin/bash
pwd
npm run build
ls -l ../static
mv ../static/index.html ../blog/templates/
git add ../blog/templates/index.html
git add ../static/*
