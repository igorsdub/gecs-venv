# Zipf Law Visualization with Python

Project to visualize Zipf's Law using Python. We will use books from [Research Software Engineering with Python](https://figshare.com/articles/dataset/Research_Software_Engineering_with_Python_Data_Files/13040516) to demonstrate the frequency of word usage in English literature.

Zipf's law is a simple pattern that often appears in language: a small number of words are used very often, while most words are used rarely. In a book, words like "the", "and", and "of" usually dominate the top of the frequency table, and the counts then drop off quickly.

This project makes that pattern visible by counting words in a text and plotting the most frequent ones as a histogram.

```mermaid
flowchart LR
    Book["Book (.txt)"] --> Words["Words"]
    Words --> Counts["Word Counts (.tsv)"]
    Counts --> Histogram["Histogram (.html + .png)"]
```

The project reads a plain-text book, extracts words, counts how often each word appears, and then turns the top counts into figures you can inspect visually.

## Project Structure

```text
.
├── books                           <-- Text files of books used for analysis
│   ├── dracula.txt
│   ├── frankenstein.txt
│   ├── jane_eyre.txt
│   ├── moby_dick.txt
│   ├── README.md                   <-- README for the book files
│   ├── sense_and_sensibility.txt
│   ├── sherlock_holmes.txt
│   └── time_machine.txt
├── .python-version                 <-- Project Python version pin
├── counts                          <-- Word count .tsv data
├── figures                         <-- Bar plots of word counts
├── pyproject.toml                  <-- Project metadata and dependencies
├── README.md                       <-- README for the project
├── uv.lock                         <-- Locked dependency versions
└── scripts                         <-- Scripts directory
    ├── count_words.py              <-- Counts word frequencies in a book
    ├── get_summary.py              <-- Extracts book summary metadata
    ├── plot_counts.py              <-- Creates HTML and PNG figures
    └── run_book_analysis.py        <-- Runs the full workflow for one book
```

## Set up the project

Create the virtual environment and install the project dependency with:

```bash
uv sync
```

This creates `.venv` and `uv.lock` for the project.

Activate the environment:

```bash
source .venv/bin/activate
```

When you are done, leave the environment with:

```bash
deactivate
```

## Usage

To run the whole pipeline for one book:

```bash
python scripts/run_book_analysis.py books/dracula.txt
```

This writes:

- `counts/dracula.tsv`
- `figures/dracula.html`
- `figures/dracula.png`

If you want to run the steps one by one, use the activated virtual environment and regular `python` commands.

First, you can get a summary of the books available:

```bash
python scripts/get_summary.py books/dracula.txt
```

Run the following command to generate a list of word counts:

```bash
python scripts/count_words.py books/dracula.txt counts/dracula.tsv
```

Finally, create both the interactive HTML figure and the PNG histogram:

```bash
python scripts/plot_counts.py counts/dracula.tsv figures/dracula.html
```

This produces:

- `figures/dracula.html`
- `figures/dracula.png`

Open the generated HTML file in your web browser to view the interactive bar chart. Either use **Show Preview** by right-clicking on the figure file in VS Code or open the file in your file browser, e.g. Finder, as a regular file. The PNG file gives you a quick static version of the same result.

Now, you can try to do the same for other books in the `books/` directory! Later on we will see how to automate this process for all books.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## References

- [Research Software Engineering with Python Data Files](https://figshare.com/articles/dataset/Research_Software_Engineering_with_Python_Data_Files/13040516)
- [Make a README](https://www.makeareadme.com/)
- [uv documentation](https://docs.astral.sh/uv/)

## Install uv

If you do not already have `uv`, install it first.

On macOS, Linux, and Ubuntu under WSL:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then reload your shell.

Ubuntu users:

```bash
source ~/.bashrc
```

macOS users:

```zsh
source ~/.zshrc
```

To verify the installation, run either:

```bash
uv --version
```

or:

```bash
which uv
```

To view the installed dependency tree for this project, run:

```bash
uv tree
```

To inspect the dependency graph in a platform-independent way, run:

```bash
uv tree --universal
```

This is useful when you want to see exactly what `uv` resolved from the project manifest and lockfile.
