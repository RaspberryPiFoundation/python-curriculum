#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUT=output
pushd $DIR
rm -fR $OUT
mkdir -p $OUT


legal="UK_LEGAL.md"

for f in ../en-GB/lessons/*/*.md;
do
	base=`basename "$f"`
	output="lesson${base%%.*}.html"
	cat "$f" "$legal" | pandoc -f markdown_github -t html5  -s --highlight-style pygments \
		-c css/codeclub.css \
		 --section-divs \
		 -o "$OUT/$output"
done

cp -r css $OUT
cp *.svg $OUT


