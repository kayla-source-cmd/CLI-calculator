# CLI Calculator

A simple Python command-line calculator that supports addition, subtraction, multiplication, and division.

## Features

- Non-interactive CLI usage: `python3 cli.py 10 + 5`
- Interactive fallback mode when no arguments are provided
- Clear error handling for invalid input and division by zero
- Installable via pip using `pyproject.toml`

## Installation

Clone the project and install it locally:

```bash
git clone <repository-url>
cd CLI-calculator
python3 -m pip install .
```

## Usage

### Non-interactive mode

```bash
python3 cli.py 10 + 5
python3 cli.py 9 / 3
python3 cli.py 8 * 7
```

Example output:

```text
Result: 15
```

### Interactive mode

```bash
python3 cli.py
```

Then enter:

```text
enter first number->10
enter operator (+, -, *, /)->+
enter second number->5
```

Example output:

```text
Result: 15
```

### Help

```bash
python3 cli.py --help
```

## Project structure

- `calculator_logic.py`: arithmetic functions
- `cli.py`: CLI entry point and input validation
- `test_calculator.py`: unit tests
- `pyproject.toml`: packaging metadata for pip installation

## Notes

The calculator raises a `ZeroDivisionError` for division by zero and the CLI converts that into a clean logged error message. This keeps the arithmetic logic consistent and predictable while allowing the command-line layer to handle user-friendly output.
