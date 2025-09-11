
#!/usr/bin/env python
"""
clean_book.py
----------------
Removes Project Gutenberg headers and footers from a plain-text file, saving the cleaned text to a new file.
Usage:
    python clean_book.py <input-file> <output-file>
"""

import sys
from typing import List

def load_text(filename: str) -> List[str]:
    """
    Load lines from a plain-text file and return them as a list, with trailing newlines stripped.

    Args:
        filename (str): Path to the input text file.

    Returns:
        List[str]: List of lines from the file.
    """
    with open(filename, encoding="utf-8") as f:
        return f.read().splitlines()

def save_text(filename: str, text: str) -> None:
    """
    Save a string to a plain-text file.

    Args:
        filename (str): Path to the output text file.
        text (str): Text to write to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def strip_headers(text: List[str]) -> str:
    """
    Strip Project Gutenberg headers and footers from the text.

    Args:
        text (List[str]): List of lines from the file.

    Returns:
        str: Cleaned text with headers/footers removed.
    """
    GUTENBERG_TEXT = "PROJECT GUTENBERG EBOOK "
    in_text = False
    output: List[str] = []

    for line in text:
        if GUTENBERG_TEXT in line:
            if not in_text:
                in_text = True
            else:
                break
        elif in_text:
            output.append(line)
    return "\n".join(output).strip()

def main():
    """
    Main entry point for the script. Cleans a Project Gutenberg text file.
    """
    if len(sys.argv) < 3:
        print("Usage: python clean_book.py <input-file> <output-file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    text = load_text(input_file)
    cleaned_text = strip_headers(text)
    save_text(output_file, cleaned_text)

if __name__ == "__main__":
    main()
