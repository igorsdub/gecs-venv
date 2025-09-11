
#!/usr/bin/env python
"""
count_words.py
----------------
Counts word frequencies in a plain-text file and saves the results as a CSV file using pandas.
Usage:
    python count_words.py <input-file> <output-file> [min_length]
"""

import sys
import pandas as pd
import re
from typing import List

DELIMITERS = r"[\.\,;:\?\$@\^<>#%`!\*\-=\(\)\[\]\{\}/\\\"']"

def load_text(filename: str) -> List[str]:
    """
    Load lines from a plain-text file and return them as a list, with trailing newlines stripped.
    """
    with open(filename, encoding="utf-8") as f:
        return f.read().splitlines()

def save_word_counts(filename: str, df: pd.DataFrame) -> None:
    """
    Save a DataFrame of word counts to a CSV file.
    """
    df.to_csv(filename, index=False)

def calculate_word_counts(lines: List[str], min_length: int = 1) -> pd.DataFrame:
    """
    Given a list of strings, parse each string and create a DataFrame of word counts.
    DELIMITERS are removed before the string is parsed. The function is case-insensitive
    and words in the dictionary are in lower-case.
    """
    words = []
    for line in lines:
        # Remove delimiters and split into words
        clean_line = re.sub(DELIMITERS, " ", line)
        words.extend([w.lower().strip() for w in clean_line.split() if len(w) >= min_length])
    word_series = pd.Series(words)
    counts = word_series.value_counts().reset_index()
    counts.columns = ["word", "count"]
    return counts

def word_count(input_file: str, output_file: str, min_length: int = 1) -> None:
    """
    Load a file, calculate the frequencies of each word in the file and
    save in a new file the words, counts and percentages of the total in
    descending order. Only words whose length is >= min_length are included.
    """
    lines = load_text(input_file)
    df = calculate_word_counts(lines, min_length)
    save_word_counts(output_file, df)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python count_words.py <input-file> <output-file> [min_length]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    min_length = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    word_count(input_file, output_file, min_length)
