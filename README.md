<div align="center">

# 🐍 Advent of Code: Solutions in Python

This repository is a curation of my personal solutions to the yearly "Advent of
Code" puzzles, starting from December 2024. All of the solutions in this
repository are written in the [Python](https://python.org) programming language.
<br>

</div>

## Table of Contents

- [Installation](#installation)
- [Get Started](#get-started)
- [Contributing](#contributing)

<br>

---

## Installation

This project is based on Python 3.13.0, so you can easily install it using the `pip` package manager:

```bash
# Install from origin.
$ pip install git+https://github.com/hitblast/advent-of-code-python.git
```

<br>

## Get Started

This repository provides a simple way to run and interact with the solutions for
each day of Advent of Code. It provides access to a CLI tool which can be
accessed through the `advent` / `aoc` command. A simple command example would be this:

```bash
# Run with user data.
$ advent run 3:1 --file path/to/input_data.txt

Result: <some_result>
$
```

This command **fetches the first (1) puzzle for the third (3) day of current year** and runs it.
If you want to simulate solutions for any given year, you can use the `--year` flag like this:

```bash
$ advent run 2:2 --year 2024 --file path/to/input_data.txt
```

or, you can also use the `--use-preincluded-data` flag to evaluate the results
based on the data which is given by the package (these are created on the basis
of my own personal solutions to the puzzles). Though, it is pretty much only for
testing purposes and you're better off **using the preincluded unit tests
instead.**

```bash
# Run without user data.
$ advent run 3:1 --use-preincluded-data

Result: 167090022
$
```

<br>

## Contributing

Pull requests are always welcome. If you do happen to find better, faster
solutions to the puzzles, please submit it and encourage others to attend the
yearly event as well! :D
