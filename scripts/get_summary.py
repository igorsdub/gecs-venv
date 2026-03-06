"""
This script extracts summary information from the header of a given file.
Usage: python scripts/get_summary.py <filename>
Example: python scripts/get_summary.py books/dracula.txt
"""

import sys


def extract_metadata_field(header_lines, field_name):
    """
    Extract a specific metadata field from header lines.
    
    Args:
        header_lines: List of lines from the file header
        field_name: The field to search for (e.g., 'Title', 'Author')
    
    Returns:
        The line containing the field, or None if not found
    """
    for line in header_lines:
        if field_name in line:
            return line
    return None


def get_file_summary(filename):
    """
    Extract summary information from a file header.
    
    Args:
        filename: Path to the file
    
    Returns:
        Dictionary containing metadata fields
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Extract lines 10-17 (0-indexed: 9-16)
        header_lines = lines[9:17] if len(lines) >= 17 else lines[9:]
        
        # Extract metadata fields
        fields = ['Title', 'Author', 'Language', 'Release']
        summary = {}
        
        for field in fields:
            line = extract_metadata_field(header_lines, field)
            if line:
                print(line.strip())
        
        return summary
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)
    
    get_file_summary(sys.argv[1])
