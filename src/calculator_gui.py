import tkinter as tk
from tkinter import messagebox
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Visual")
        self.calc = Calculator()
        self.expression = ""

        self.display = tk.Entry(master, width=20, font=("Arial", 24), borderwidth=2, relief="groove", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('^', 5, 1), ('√', 5, 2), ('|x|', 5, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(master, text=text, width=5, height=2, font=("Arial", 16),
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = self.evaluate_expression(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
                self.display.delete(0, tk.END)
                self.expression = ""
        elif char == '^':
            self.expression += '^'
            self.display.insert(tk.END, '^')
        elif char == '√':
            try:
                value = float(self.display.get())
                result = self.calc.sqrt(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        elif char == '|x|':
            try:
                value = float(self.display.get())
                result = self.calc.absolute(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            self.expression += str(char)
            self.display.insert(tk.END, char)

    def evaluate_expression(self, expr):
        # Substitui operadores para usar os métodos da Calculator
        if '^' in expr:
            base, exp = expr.split('^')
            return self.calc.power(float(base), float(exp))
        if '/' in expr:
            a, b = expr.split('/')
            return self.calc.divide(float(a), float(b))
        if '*' in expr:
            a, b = expr.split('*')
            return self.calc.multiply(float(a), float(b))
        if '-' in expr:
            a, b = expr.split('-')
            return self.calc.subtract(float(a), float(b))
        if '+' in expr:
            a, b = expr.split('+')
            return self.calc.add(float(a), float(b))
        return float(expr)

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()
