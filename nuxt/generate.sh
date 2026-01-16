#!/bin/bash
nuxt generate
mv ../static/nuxt/index.html ../blog/templates/
git add ../blog/templates/index.html
git add ../static/*
