"""
Plots word counts as an interactive HTML chart and a PNG histogram.
Usage: python scripts/plot_counts.py <input_file> <output_html_file>
Example: python scripts/plot_counts.py counts/dracula.tsv figures/dracula.html
"""

from pathlib import Path
import sys
from bokeh.plotting import figure, save, output_file
from bokeh.models import HoverTool
from PIL import Image, ImageDraw, ImageFont


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


def save_histogram_png(words, counts, output_png_filename):
    """Save a simple static histogram image for the top words."""
    width = 1400
    height = 900
    margin_left = 120
    margin_right = 60
    margin_top = 90
    margin_bottom = 240
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.load_default()
    label_font = ImageFont.load_default()

    max_count = max(counts)
    bar_count = len(words)
    gap = 12
    bar_width = max(18, (plot_width - gap * (bar_count - 1)) // bar_count)

    # Axes
    x0 = margin_left
    y0 = margin_top + plot_height
    x1 = margin_left + plot_width
    y1 = margin_top
    draw.line((x0, y0, x1, y0), fill="black", width=3)
    draw.line((x0, y0, x0, y1), fill="black", width=3)

    # Title and axis labels
    draw.text((width // 2 - 70, 25), "Top 20 Word Counts", fill="black", font=title_font)
    draw.text((width // 2 - 20, height - 35), "Word", fill="black", font=label_font)
    draw.text((25, margin_top - 10), "Count", fill="black", font=label_font)

    # Y-axis ticks
    tick_count = 5
    for tick_index in range(tick_count + 1):
        tick_value = round(max_count * tick_index / tick_count)
        tick_y = y0 - int(plot_height * tick_index / tick_count)
        draw.line((x0 - 10, tick_y, x0, tick_y), fill="black", width=2)
        draw.text((20, tick_y - 8), str(tick_value), fill="black", font=label_font)

    # Bars and labels
    for index, (word, count) in enumerate(zip(words, counts)):
        bar_left = x0 + index * (bar_width + gap)
        bar_right = bar_left + bar_width
        bar_top = y0 - int((count / max_count) * plot_height)
        draw.rectangle((bar_left, bar_top, bar_right, y0), fill="steelblue", outline="black")
        draw.text((bar_left, bar_top - 18), str(count), fill="black", font=label_font)

        label_image = Image.new("RGBA", (110, 24), (255, 255, 255, 0))
        label_draw = ImageDraw.Draw(label_image)
        label_draw.text((0, 0), word, fill="black", font=label_font)
        rotated_label = label_image.rotate(55, expand=True)
        image.paste(rotated_label, (bar_left - 8, y0 + 10), rotated_label)

    image.save(output_png_filename)


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

    # Save
    save(p)
    output_png_filename = make_png_filename(output_filename)
    save_histogram_png(words, counts, output_png_filename)
    print(f"Plot saved to {output_filename}")
    print(f"Histogram saved to {output_png_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    plot_word_counts(input_filename, output_filename)
