#!/bin/bash
quasar build
mv ../static/quasar/index.html ../pages/templates
git add ../pages/templates/index.html
git add ../static/quasar/*
