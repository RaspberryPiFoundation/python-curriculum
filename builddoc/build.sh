#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUT=output
pushd $DIR
mkdir -p $OUT


for f in ../en-GB/lessons/*/*.md;
do
	base=`basename "$f"`
	output="lesson${base%%.*}.html"
	pandoc -f markdown_github -t html5  -s --highlight-style pygments -c css/codeclub.css --section-divs \
		"$f" -o "$OUT/$output"
done

