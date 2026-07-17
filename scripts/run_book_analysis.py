"""
Run the full book-analysis workflow for a single book.
Usage: python scripts/run_book_analysis.py <book_file>
Example: python scripts/run_book_analysis.py books/dracula.txt
"""

from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from count_words import count_word_frequencies
from get_summary import get_file_summary
from plot_counts import plot_word_counts


def output_paths(book_filename):
    """Return output paths for the counts and figure files."""
    book_path = Path(book_filename)
    stem = book_path.stem
    counts_path = Path("counts") / f"{stem}.tsv"
    figure_path = Path("figures") / f"{stem}.html"
    counts_path.parent.mkdir(parents=True, exist_ok=True)
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    return counts_path, figure_path


def run_book_analysis(book_filename):
    """Run summary, counting, and plotting for a single book file."""
    counts_path, figure_path = output_paths(book_filename)
    get_file_summary(book_filename)
    count_word_frequencies(book_filename, str(counts_path))
    plot_word_counts(str(counts_path), str(figure_path))
    print(f"Finished analysis for {book_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <book_file>", file=sys.stderr)
        sys.exit(1)

    run_book_analysis(sys.argv[1])
