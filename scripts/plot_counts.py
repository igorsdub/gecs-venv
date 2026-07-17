"""
Plots word counts as an interactive HTML chart and a PNG histogram.
Usage: python scripts/plot_counts.py <input_file> <output_html_file>
Example: python scripts/plot_counts.py counts/dracula.tsv figures/dracula.html
"""

from pathlib import Path
from contextlib import contextmanager
import os
import sys
import tempfile
import textwrap
from bokeh.io import export_png
import bokeh.io.export as bokeh_export
from bokeh.plotting import figure, save, output_file
from bokeh.models import HoverTool
import chromedriver_binary  # noqa: F401


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


@contextmanager
def writable_bokeh_tmp_html(tmp_dir):
    """Mirror Bokeh's temp HTML helper, but use a writable temp directory."""
    tmp = tempfile.NamedTemporaryFile(
        mode="wb",
        dir=tmp_dir,
        prefix="bokeh",
        suffix=".html",
        delete=False,
    )
    try:
        yield tmp
    finally:
        os.unlink(tmp.name)


def export_png_with_writable_tmp(plot, output_png_filename):
    """Use Bokeh's export_png() with a writable temp directory."""
    original_tmp_html = bokeh_export._tmp_html
    tmp_dir = tempfile.gettempdir()
    bokeh_export._tmp_html = lambda: writable_bokeh_tmp_html(tmp_dir)
    try:
        export_png(plot, filename=output_png_filename)
    finally:
        bokeh_export._tmp_html = original_tmp_html


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

    output_path = Path(output_filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

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

    # Save HTML output
    save(p)
    output_png_filename = make_png_filename(output_filename)

    try:
        export_png_with_writable_tmp(p, output_png_filename)
    except Exception as exc:
        message = textwrap.dedent(
            f"""
            PNG export failed.

            Bokeh's export_png() requires Selenium and a compatible browser driver,
            plus Chrome/Chromium or Firefox on the system.

            Original error:
            {exc}
            """
        ).strip()
        print(message, file=sys.stderr)
        raise SystemExit(1) from exc

    print(f"Plot saved to {output_filename}")
    print(f"Histogram saved to {output_png_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    plot_word_counts(input_filename, output_filename)
