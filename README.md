# Good Enough Computing in Science (GECS) | Tutorial 1 | Virtual environments

A tutorial on use of virtual environments using [Pixi](https://pixi.sh) for reproducible research projects. Using [The Odyssey by Homer](https://www.gutenberg.org/cache/epub/1727/pg1727.txt) from [The Project Gutenberg](https://www.gutenberg.org/) we will perform a simple data analysis pipeline on the book's text.

## Organization

```text
├── LICENSE                 <- Open-source license
├── README.md               <- The top-level README for researchers using this project.
├── pixi.toml               <- Project's virtual environment configuration file with package metadata.
├── pixi.lock               <- Project's vrtual environemnt lockfile.
├── data
│   ├── processed           <- The final, canonical data sets for analysis.
│   └── raw                 <- The original, immutable data dump.
│       └── book.txt        <- A raw book text.
│
├── analyzed                <- Processed data that has been analyzed.
│  
├── scripts                 
│   ├── clean_book.py       <- Removes Project Gutenberg headers/footers from a text file.
│   ├── count_words.py      <- Counts word frequencies in the clean text and saves as CSV.
│   └── plot_counts.py      <- Plots histogram of word counts from CSV.
│
└── results                 <- Generated word count histogram by the scripts from the raw data.
```

## Installation

Use the package manager [pixi](https://pixi.sh) to install the virtual enviroemnet for this project.

```bash
pixi install
```

## Usage

To execute the project pipeline via command-line interface (CLI), first active the virtual environement shell

```bash
pixi shell
```

Next, run the following commands in the given order:

```bash
python clean_book.py data/raw/book.txt data/processed/book.txt
python count_words.py data/processed/book.txt analyzed/word_count.csv
python plot_histogram.py analyzed/word_count.csv results/histogram.pdf
```

The word count histogram, `histogram.pdf`, can be found in `results` folder.

For running each of the steps using Pixi tasks execute the following:

```bash
pixi run process
pixi run analyze
pixi run plot
```

In order to run all of these tasks together, use a convieniet task that combines the above together:

```bash
pixi run all
```

You might wish to clean the folders before you do so with

```bash
pixi run clean
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate. To be added...

## License

[MIT](https://choosealicense.com/licenses/mit/)

## References
1. [Make a README](https://www.makeareadme.com/)