# icpc-pucp-training

Minimalist infrastructure for managing competitive programming lectures and contest generation.

## Prerequisites
- **uv**: modern Python package manager.
- Python 3.14+
- Make

## Installation

Clone the repository.
```bash
$ git clone git@github.com:ManuelLoaizaV/icpc-pucp-training.git
$ cd icpc-pucp-training
```

Install dependencies and initialize the data directory.
```bash
$ make setup
```

## Usage
To generate a new contest, specify the year, lecture tag, and the number of problems for each difficulty level.
```bash
$ make generate YEAR=2026 LECTURE=segment-tree EASY=2 MEDIUM=2 HARD=1
```

The contest will be persisted in `data/timeline_{YEAR}.csv`.
