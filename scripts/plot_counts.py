"""
Plots word counts as an interactive HTML chart and a PNG histogram.
Usage: python scripts/plot_counts.py <input_file> <output_html_file>
Example: python scripts/plot_counts.py counts/dracula.tsv figures/dracula.html
"""

from pathlib import Path
import sys

import altair as alt


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


def make_png_filename(output_html_filename):
    """Create the PNG output path from the HTML output path."""
    return str(Path(output_html_filename).with_suffix(".png"))


def plot_word_counts(input_filename, output_filename):
    """
    Create an interactive Altair bar chart of word counts.

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

    output_path = Path(output_filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = [{"word": word, "count": count} for word, count in zip(words, counts)]
    chart = (
        alt.Chart(alt.Data(values=data))
        .mark_bar(color="steelblue")
        .encode(
            x=alt.X("word:N", title="Word", sort=None),
            y=alt.Y("count:Q", title="Count"),
            tooltip=[alt.Tooltip("word:N", title="Word"), alt.Tooltip("count:Q", title="Count")],
        )
        .properties(title="Word Counts", width=1000, height=600)
        .configure_axis(labelFontSize=14, titleFontSize=14, labelAngle=-45)
    )

    chart.save(str(output_path))
    output_png_filename = make_png_filename(output_filename)
    chart.save(output_png_filename)

    print(f"Plot saved to {output_filename}")
    print(f"Histogram saved to {output_png_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    plot_word_counts(input_filename, output_filename)
