#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUT=output
pushd $DIR
rm -fR $OUT
mkdir -p $OUT


legal="UK_LEGAL.md"

PANDOC_HTML="pandoc -f markdown_github -t html5 -s --highlight-style pygments -c css/codeclub.css  --section-divs"

PANDOC_PDF="pandoc -f markdown_github -t latex  --latex-engine=pdflatex"


for f in ../en-GB/lessons/*/*.md;
do
	base=`basename "$f"`
	output="lesson${base%%.*}.html"
	cat "$f" "$legal" | $PANDOC_HTML -o "$OUT/$output"
	pdf="lesson${base%%.*}.pdf"
	cat "$f" "$legal" | $PANDOC_PDF  -o "$OUT/$pdf"

done

cat "../en-GB/volunteer resources/resources_and_gotchas.md" | $PANDOC_HTML -o "$OUT/guide.html"
cat "../en-GB/volunteer resources/resources_and_gotchas.md" | $PANDOC_PDF -o "$OUT/guide.pdf"

cp -r css $OUT
cp *.svg $OUT


