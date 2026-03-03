# Zipf Law Visualization with Command Line

> Title should be concise and descriptive, followed by a short description of what the project does. Think of some one who stumbles upon your project and wants to quickly understand its purpose.

Project to visualize Zipf's Law using command line tools. We will use books from [Research Software Engineering with Pyhton](https://figshare.com/articles/dataset/Research_Software_Engineering_with_Python_Data_Files/13040516) to demonstrate the frequency of word usage in English literature.

## Project Structure

> Briefly describe the structure of your project, including important directories and files.

```bash
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
    ├── count_words.sh              <-- Counts occurences of word in a books
    ├── get_summary.sh              <-- Gets a book summary
    └── plot_counts.sh              <-- Plots count histogram in terminal window
```

## Prerequisites

> Before running any code, list any prerequisites that need to be installed or configured.

You will use [YouPlot](https://github.com/red-data-tools/YouPlot), a command line plotting tool. Make sure you have it installed. You can delete it after the tutroial if you wish.

![YouPlot bar plot](https://user-images.githubusercontent.com/5798442/101999903-d36a2d00-3d24-11eb-9361-b89116f44122.png)

For macOS, you can install YouPlot using [Homebrew](https://brew.sh):

```bash
brew install youplot
```

For Linux or WSL you will need to enter your password:

```bash
sudo apt-get install youplot
```

## Usage

> Provide step-by-step instructions on how to use the project. Overexplaining is better then underexplaining. The future you will be thankful 😊.

First, you can get a summary of the books available:

```bash
bash scripts/get_summary.sh books/dracula.txt
```

The main workflow consists of counting the words in a book and then plotting the results.

```mermaid
flowchart LR
    Book --> Counts --> Plot
```

>[!TIP]
> For more diagrams like this, check out [Mermaid](https://mermaid-js.github.io/mermaid/#/) and [a GitHub tuttorial](https://github.blog/developer-skills/github/include-diagrams-markdown-files-mermaid/).

Run the following command to generate a list of word counts:

```bash
bash scripts/count_words.sh books/dracula.txt > counts/dracula.tsv
```
>[!TIP]
> You can use `.tsv` (Tab-Separated Values) file format when storing and handling tabular data. It’s a simple, plain-text file format, where information is organized in rows and columns, and tabs are used as separators. Compared to `.csv`, `.tsv` files avoid many issues related to commas appearing inside data values.

Finally, you can plot the results using YouPlot:

```bash
bash scripts/plot_counts.sh counts/dracula.tsv 2> figures/dracula.plot
```

> [!NOTE]
> We are using `2>` to redirect the standard error output to a file because YouPlot writes plots to standard error by default. You can learn about `STDOUT` and `STDERR` [here](https://en.wikipedia.org/wiki/Standard_streams).

To access the plots, open the file in directory as a text file or print it to the terminal:

```bash
cat figures/dracula.plot
```

Now, you can try to do the same for other books in the `books/` directory! Later on we will see how to automate this process for all books.

## Contributing

> This section is appropriate for open source projects hosted online, such as on GitHub.

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

> It is good practice to include a license for open source projects.

[MIT](https://choosealicense.com/licenses/mit/)

## References

> Put references here for proper attribution and further reading.

- [Research Software Engineering with Python Data Files](https://figshare.com/articles/dataset/Research_Software_Engineering_with_Python_Data_Files/13040516)
- [YouPlot](https://github.com/red-data-tools/YouPlot)
- [Markdown Notice Blocks](https://www.freecodecamp.org/news/how-to-create-notice-blocks-in-markdown/)

## Why README?

> Because no one can read your mind (yet)
>
> [Make a README](https://www.makeareadme.com/)

If there's one file you should always include with your project, it's a README. A good README helps others understand what your project is about, how to use it, and how to contribute. It also serves as a reference for you in the future when you come back to the project after some time away. See [Make a README](https://www.makeareadme.com/) for more information.

*This README used the [Make a README template](https://www.makeareadme.com/#template-1).*
