#!/usr/bin/env python3
"""
Plots word counts as an interactive bar chart using Bokeh.
Usage: python scripts/plot_counts.py <input_file> <output_file>
Example: python scripts/plot_counts.py counts/dracula.tsv dracula_plot.html
"""

import sys
from bokeh.plotting import figure, save, output_file
from bokeh.models import HoverTool


def parse_counts_file(filename):
    """
    Parse a word counts file.

    Expects format: count<tab>word or count<space>word

    Args:
        filename: Path to the counts file

    Returns:
        Tuple of (words, counts) lists
    """
    words = []
    counts = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                # Split by whitespace (tab or spaces)
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        count = int(parts[0])
                        word = parts[1]
                        counts.append(count)
                        words.append(word)
                    except ValueError:
                        continue

    except FileNotFoundError:
        print("File not found!", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    return words, counts


def plot_word_counts(input_filename, output_filename):
    """
    Create an interactive Bokeh bar chart of word counts.

    Args:
        input_filename: Path to the counts file
        output_filename: Path to the output HTML file
    """
    words, counts = parse_counts_file(input_filename)

    if not words:
        print("No data found in file!", file=sys.stderr)
        sys.exit(1)

    # Take top 20
    words = words[:20]
    counts = counts[:20]

    # Set up output file
    output_file(output_filename)

    # Create figure
    p = figure(
        x_range=words,
        title="Word Counts",
        width=1000,
        height=600,
        toolbar_location="right",
    )

    # Add bar chart
    p.vbar(x=words, top=counts, width=0.8, color="steelblue")

    # Customize with scaled fonts (1.2x)
    p.title.text_font_size = "14pt"
    p.xaxis.axis_label = "Word"
    p.xaxis.axis_label_text_font_size = "12pt"
    p.xaxis.major_label_text_font_size = "12pt"
    p.yaxis.axis_label = "Count"
    p.yaxis.axis_label_text_font_size = "12pt"
    p.yaxis.major_label_text_font_size = "12pt"
    p.xaxis.major_label_orientation = 0.785  # 45 degrees

    # Add hover tool
    hover = HoverTool(tooltips=[("Word", "@x"), ("Count", "@top")])
    p.add_tools(hover)

    # Save
    save(p)
    print(f"Plot saved to {output_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    plot_word_counts(input_filename, output_filename)
