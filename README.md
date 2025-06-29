# Basic Calculator Application

This is a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, division, power, square root, and absolute value. It includes both a command-line interface and a modern graphical interface using ttkbootstrap.

## Project Structure

```
calculator-app
├── src
│   ├── calculator.py         # Calculator class with arithmetic methods
│   ├── calculator_gui.py     # Graphical interface using ttkbootstrap
│   └── __init__.py           # Marks the src directory as a package
├── tests
│   └── test_calculator.py    # Unit tests for the Calculator class
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage (Command Line)

To use the calculator in the terminal, run:

```
python src/calculator.py
```

Follow the on-screen instructions to perform calculations.

## Usage (Graphical Interface)

To launch the visual calculator, run:

```
python src/calculator_gui.py
```

A window will open with buttons for numbers, basic operations, power (^), square root (√), and absolute value (|x|). You can change the theme by editing the `themename` parameter in the code.

## Running Tests

To run the unit tests for the Calculator class, use:

```
pytest tests/test_calculator.py
```

Make sure you have `pytest` installed.

## License

This project is open source and available under the MIT License.