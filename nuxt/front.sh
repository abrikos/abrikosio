#!/bin/bash
echo "FFFFFFFFFFFFFF"
rm -fr ../static/_nuxt;
mv ../blog/templates/static/index.html ../blog/templates/index.html
cp -r ../blog/templates/static/* ../static/
git add ../blog/templates/index.html
git add ../static/*