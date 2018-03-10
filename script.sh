#!/bin/bash

for f in _posts/2*.md;
do
	python converter/convert.py $f
done
