#! /bin/bash
URL=$1
FILENAME=$(basename "URL")
echo "Downloading $URL..."
curl -O "$FILENAME" "$URL"

tar -xzvf "$FILENAME"

TSV_file=$(find , -type f -name "*.tsv | head -n 1)
CSV_file="${TSV_file%.tsv}.csv"
tr '\t' ',' <"TSV_file"> "$CSV_file"

