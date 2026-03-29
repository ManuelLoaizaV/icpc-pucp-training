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

## For new competitors

If you are on Windows, follow this [tutorial to install and setup VSCode and a C++ compiler](https://code.visualstudio.com/docs/cpp/config-mingw).

If you're on Linux, you can proceed directly to the next steps.

Create an account on [vjudge](https://vjudge.net/).

Join our [public group](https://vjudge.net/group/pucp-ac).

To participate, click on the current weekly contest, select a problem, and submit your solution (ensure correct language/compiler).

We use C++ as it is the standard for competitive programming.
VSCode is recommended as it is user-friendly for beginners
and supported in in-person competitions.

AI assistance is prohibited to ensure fair learning and problem-solving.
Deactivate AI features in your IDE and avoid ChatGPT, Gemini, or similar tools.
