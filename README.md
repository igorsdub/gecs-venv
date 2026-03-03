# Zipf Law Visualization with Python

Project to visualize Zipf's Law using Python. We will use books from [Research Software Engineering with Pyhton](https://figshare.com/articles/dataset/Research_Software_Engineering_with_Python_Data_Files/13040516) to demonstrate the frequency of word usage in English literature.

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
├── counts                          <-- Word count .tsv data
├── figures                         <-- Bar plots of word counts
├── README.md                       <-- README for the project
└── scripts                         <-- Scripts directory
    ├── count_words.py              <-- Counts word frequencies in a book
    ├── get_summary.py              <-- Extracts book summary metadata
    └── plot_counts.py              <-- Creates interactive word frequency plots
```

## Prerequisites

To install required packages use Pixi:

```bash
pixi install
```

## Usage

First, you can get a summary of the books available:

```bash
python scripts/get_summary.py books/dracula.txt
```

The main workflow consists of counting the words in a book and then plotting the results.

```mermaid
flowchart LR
    Book --> Counts --> Plot
```

Run the following command to generate a list of word counts:

```bash
python scripts/count_words.py books/dracula.txt counts/dracula.tsv
```

Finally, you can plot the results:

```bash
python scripts/plot_counts.py counts/dracula.tsv figures/dracula.html
```

Then open the generated HTML file in your web browser to view the interactive bar chart. Either use **Show Preview** by right-clicking on the figure file in VS Code or open the file in your file browser, e.g. Finder, as a regular file. In the latter case, the plot will open in your defualt web browser.

Now, you can try to do the same for other books in the `books/` directory! Later on we will see how to automate this process for all books.

### Pixi Tasks

Besides installing and tracking packages, Pixi can store Bash commands (You can check them in `pixi.toml` under **Tasks**) and execute them using `pixi run` option. For `dracula.txt` book the following commands will get summary, count words, and plot those word counts.

```bash
pixi run summarize
pixi run count
pixi run plot
```

or simply run the below command that combines the commands above together:

```bash
pixi run all
```

Right now, it only works for one book and they are hard coded. In the next session, we will see how the same commands can be applied to all books automatically without a need to specify filename explitly using Make.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## References

- [Research Software Engineering with Python Data Files](https://figshare.com/articles/dataset/Research_Software_Engineering_with_Python_Data_Files/13040516)
- [Make a README](https://www.makeareadme.com/)
- [Pixi](https://www.pixi.sh)
