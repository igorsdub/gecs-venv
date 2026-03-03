#!/usr/bin/env python3
"""
This script counts the number of individual words in a given file.
Usage: python scripts/count_words.py <filename>
Example: python scripts/count_words.py books/dracula.txt
"""

import sys
import re
from collections import Counter


def extract_words(text):
    """
    Extract all alphanumeric words from text and convert to lowercase.
    
    Args:
        text: The text content to process
    
    Returns:
        List of words in lowercase
    """
    # Replace non-alphanumeric characters with spaces and split
    words = re.findall(r'\b[a-z0-9]+\b', text.lower())
    return words


def count_word_frequencies(filename):
    """
    Count word frequencies in a file and print sorted results.
    
    Args:
        filename: Path to the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Extract words
        words = extract_words(text)
        
        # Count frequencies
        word_counts = Counter(words)
        
        # Sort by count descending, then alphabetically for ties
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        
        # Print results in format: count word
        for word, count in sorted_counts:
            print(f"{count:7d} {word}")
    
    except FileNotFoundError:
        print(f"File not found!", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)
    
    filename = sys.argv[1]
    count_word_frequencies(filename)
