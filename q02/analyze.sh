#!/bin/bash

if [ ! -f "$1" ]; then
    echo "Error: file not found: $1" >&2
    exit 1
fi

echo "Top 2 5xx paths:"

awk -F',' 'NR > 1 && $4 >= 500 && $4 < 600 {count[$3]++} END {for (path in count) print count[path], path}' "$1" |
sort -k1,1nr -k2,2 |
head -n 2

awk -F',' 'NR > 1 {sum += $5; count++} END {printf "Average latency: %.2f ms\n", sum / count}' "$1"
