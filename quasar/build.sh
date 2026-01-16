#!/bin/bash
quasar build
mv ../static/quasar/index.html ../blog/templates
git add ../blog/templates/index.html
git add ../static/*
