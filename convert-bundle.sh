#!/bin/bash
set -euo pipefail

curl -o lab3-bundle.tar.gz https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

# decompress file
tar -xzf lab3-bundle.tar.gz

# awk can remove blank / whitespace-only lines
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned_data.tsv

sed 's/\t/,/g' cleaned_data.tsv > cleaned_data.csv

LINE_COUNT=$(($(wc -l < cleaned_data.csv) - 1))
echo "Number of rows: $LINE_COUNT"

tar -czvf converted-archive.tar.gz cleaned_data.csv
