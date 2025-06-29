# Basic Calculator Application

This is a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Project Structure

```
calculator-app
├── src
│   ├── calculator.py       # Contains the Calculator class with arithmetic methods
│   └── __init__.py         # Marks the src directory as a package
├── tests
│   └── test_calculator.py   # Unit tests for the Calculator class
├── requirements.txt         # Lists project dependencies
└── README.md                # Project documentation
```

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To use the calculator, you can import the `Calculator` class from the `src.calculator` module in your Python scripts:

```python
from src.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
```

## Running Tests

To run the unit tests for the Calculator class, use the following command:

```
pytest tests/test_calculator.py
```

Make sure you have `pytest` installed, which can be added to your `requirements.txt` file.

## License

This project is open source and available under the MIT License.