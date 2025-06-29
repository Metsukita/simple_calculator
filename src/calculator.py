# Classe que representa uma calculadora
class Calculator:
    # Método para somar dois números
    def add(self, a, b):
        return a + b

    # Método para subtrair dois números
    def subtract(self, a, b):
        return a - b

    # Método para multiplicar dois números
    def multiply(self, a, b):
        return a * b

    # Método para dividir dois números
    # Lança um erro se o divisor for zero
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b