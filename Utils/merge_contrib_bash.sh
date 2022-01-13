#!/usr/bin/env bash

CONTENT_URL='https://github.com/demisto/content.git'

git remote add upstream_content $CONTENT_URL
git fetch upstream_content
git checkout master
git rebase upstream_content/master
git push -f origin master
git pull origin master
