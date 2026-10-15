# querying-with-sql-and-python
Analyze the Chinook database using SQL and Python to answer business questions and present the results.

## Features

- Answer three business questions:
  - Identify the 10 best-selling tracks
  - Find the country with the highest revenue
  - Identify the top-performing sales employee
- Display the results as Pandas DataFrames
- Visualize the results using bar charts

## Requirements

- Python 3.10+

## Technologies

- Python
- sqlite3
- Pandas
- Matplotlib

## Installation

### Clone the repository

```bash
git clone https://github.com/maxim092091-eng/querying-with-sql-and-python.git
``` 

### Navigate to the project directory

```bash
cd querying-with-sql-and-python
``` 

### Create a virtual environment

#### On Windows

```bash
py -m venv .venv
```

#### On Linux/macOS

```bash
python3 -m venv .venv
```

### Activate the virtual environment

#### On Windows

```bash
.venv\Scripts\activate
```

#### On Linux/macOS

```bash
source .venv/bin/activate
```

### Install the project

```bash
python -m pip install .
```

## Usage

Run the application:

```bash
chinook-analysis
```

## Project Structure

```text
querying-with-sql-and-python/
├── data/
|    └── Chinook_Sqlite.sqlite
├── src/
│   └── querying_with_sql_and_python/
│       ├── data_analysis.py
│       ├── database.py
│       └── main.py
├── tests/
│   └── test_database.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Tests

Run the tests with:

```bash
pytest
```

## Project

This project was built following the [Querying with SQL & Python](https://roadmap.sh/projects/querying-sql-python) project requirements from Roadmap.sh.

## License

This project is licensed under the MIT License.

## Author

Created by [Maxim](https://github.com/maxim092091-eng).

