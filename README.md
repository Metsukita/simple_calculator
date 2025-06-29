# Basic Calculator Application

This is a simple calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Project Structure

```
calculator-app
├── src
│   ├── calculator.py       # Contains the Calculator class with arithmetic methods
│   ├── calculator_gui.py   # Contains the code for the graphical user interface
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

## Graphical User Interface (GUI)

This project also includes a graphical calculator using Tkinter.

### Running the Visual Calculator

To launch the visual calculator, run:

```
python src/calculator_gui.py
```

A window will open com botões para números, operações básicas, potência (^), raiz quadrada (√) e valor absoluto (|x|).

### Example

- Clique nos botões para montar a expressão e pressione '=' para ver o resultado.
- Para raiz quadrada ou valor absoluto, digite o número e clique no respectivo botão.

> Requer Python com Tkinter (já incluso na maioria das instalações padrão).

## License

This project is open source and available under the MIT License.