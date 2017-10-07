#!/bin/sh

sudo apt-get install $(grep -E "^\s*#>" requirements.txt  | tr "\n" " " | tr -d "#>")

sudo pip install -r requirements.txt
