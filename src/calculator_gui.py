# Import standard Tkinter (still needed for some functions)
import tkinter as tk
# Import messagebox to show errors
from tkinter import messagebox
# Import the Calculator class created earlier
from calculator import Calculator
# Import ttkbootstrap for a prettier interface
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Class for the calculator graphical interface
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Visual Calculator")  # Window title
        self.calc = Calculator()           # Create a calculator instance
        self.expression = ""               # Stores the typed expression

        # Text field where the number or result appears
        self.display = tb.Entry(master, width=20, font=("Arial", 24), bootstyle="info", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # List of buttons: text, row, column
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('^', 5, 1), ('√', 5, 2), ('|x|', 5, 3)
        ]

        # Create each button on the screen
        for (text, row, col) in buttons:
            tb.Button(
                master, text=text, width=5, bootstyle="primary outline",
                command=lambda t=text: self.on_button_click(t)  # When clicked, calls the function with the button text
            ).grid(row=row, column=col, padx=5, pady=5)

    # Function called when any button is clicked
    def on_button_click(self, char):
        if char == 'C':  # Clear all
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':  # Calculate result
            try:
                result = self.evaluate_expression(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.display.delete(0, tk.END)
                self.expression = ""
        elif char == '^':  # Power
            self.expression += '^'
            self.display.insert(tk.END, '^')
        elif char == '√':  # Square root
            try:
                value = float(self.display.get())
                result = self.calc.sqrt(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == '|x|':  # Absolute value
            try:
                value = float(self.display.get())
                result = self.calc.absolute(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:  # Numbers and operators
            self.expression += str(char)
            self.display.insert(tk.END, char)

    # Function that interprets the typed expression and does the calculation
    def evaluate_expression(self, expr):
        # If there's power
        if '^' in expr:
            base, exp = expr.split('^')
            return self.calc.power(float(base), float(exp))
        # If there's division
        if '/' in expr:
            a, b = expr.split('/')
            return self.calc.divide(float(a), float(b))
        # If there's multiplication
        if '*' in expr:
            a, b = expr.split('*')
            return self.calc.multiply(float(a), float(b))
        # If there's subtraction
        if '-' in expr:
            a, b = expr.split('-')
            return self.calc.subtract(float(a), float(b))
        # If there's addition
        if '+' in expr:
            a, b = expr.split('+')
            return self.calc.add(float(a), float(b))
        # If it's just a number
        return float(expr)

# Program entry point
if __name__ == "__main__":
    # Create the main window with a nice theme
    app = tb.Window(themename="superhero")
    gui = CalculatorGUI(app)
    app.mainloop()
