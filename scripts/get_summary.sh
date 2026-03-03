#!/usr/bin/bash
# This script extracts summary information from the header of a given file.
# Usage: bash scripts/get_summary.sh <filename>
# Example: bash scripts/get_summary.sh data/dracula.txt

head -n 17 $1 | tail -n 8 | grep Title
head -n 17 $1 | tail -n 8 | grep Author
head -n 17 $1 | tail -n 8 | grep Language
head -n 17 $1 | tail -n 8 | grep Release
