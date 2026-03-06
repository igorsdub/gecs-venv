"""
This script counts the number of individual words in a given file.
Usage: python scripts/count_words.py <input_file> <output_file>
Example: python scripts/count_words.py books/dracula.txt counts/dracula.tsv
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
    words = re.findall(r"\b[a-z0-9]+\b", text.lower())
    return words


def count_word_frequencies(input_filename, output_filename):
    """
    Count word frequencies in a file and write sorted results.

    Args:
        input_filename: Path to the input file
        output_filename: Path to the output file
    """
    try:
        with open(input_filename, "r", encoding="utf-8") as f:
            text = f.read()

        # Extract words
        words = extract_words(text)

        # Count frequencies
        word_counts = Counter(words)

        # Sort by count descending, then alphabetically for ties
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

        # Prepare output lines
        output_lines = [f"{count:7d} {word}" for word, count in sorted_counts]

        # Write results to file
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines) + "\n")
        print(f"Results written to {output_filename}")

    except FileNotFoundError:
        print("File not found!", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    count_word_frequencies(input_filename, output_filename)
