# Zipf Law Visualization with Python

Project to visualize Zipf's Law using Python. We will use books from [Research Software Engineering with Python](https://figshare.com/articles/dataset/Research_Software_Engineering_with_Python_Data_Files/13040516) to demonstrate the frequency of word usage in English literature.

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
    └── plot_counts.py              <-- Creates interactive word frequency plots
```

## Set up the project

Create the virtual environment and install the project dependency with:

```bash
uv sync
```

This creates `.venv` and `uv.lock` for the project.

If you want an activated shell session, you can do that after syncing:

```bash
source .venv/bin/activate
```

When you are done, leave the environment with:

```bash
deactivate
```

You do not need activation for the commands below, because `uv run` can execute them directly inside the project environment.

## Usage

First, you can get a summary of the books available:

```bash
uv run python scripts/get_summary.py books/dracula.txt
```

The main workflow consists of counting the words in a book and then plotting the results.

```mermaid
flowchart LR
    Book --> Counts --> Plot
```

Run the following command to generate a list of word counts:

```bash
uv run python scripts/count_words.py books/dracula.txt counts/dracula.tsv
```

Finally, you can plot the results:

```bash
uv run python scripts/plot_counts.py counts/dracula.tsv figures/dracula.html
```

Then open the generated HTML file in your web browser to view the interactive bar chart. Either use **Show Preview** by right-clicking on the figure file in VS Code or open the file in your file browser, e.g. Finder, as a regular file. In the latter case, the plot will open in your default web browser.

Now, you can try to do the same for other books in the `books/` directory! Later on we will see how to automate this process for all books.

## Inspect dependencies

To view the installed dependency tree for this project, run:

```bash
uv tree
```

To inspect the dependency graph in a platform-independent way, run:

```bash
uv tree --universal
```

This is useful when you want to see exactly what `uv` resolved from the project manifest and lockfile.

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
