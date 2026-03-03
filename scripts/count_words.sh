#!/usr/bin/bash
# This script counts the number of individual words in a given file.
# Usage: bash scripts/count_words.sh <filename>
# Example: bash scripts/count_words.sh data/dracula.txt

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

FILENAME=$1

if [ ! -f "$FILENAME" ]; then
    echo "File not found!"
    exit 1
fi

tr -c '[:alnum:]' '[\n*]' < "$FILENAME" | tr '[:upper:]' '[:lower:]' | grep -v '^$' | sort | uniq -c | sort -nr
