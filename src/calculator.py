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

    # Método para calcular a potência de um número
    def power(self, a, b):
        return a ** b

    # Método para calcular a raiz quadrada de um número
    def sqrt(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular a raiz de número negativo.")
        return a ** 0.5

    # Método para calcular o módulo (valor absoluto) de um número
    def absolute(self, a):
        return abs(a)

if __name__ == "__main__":
    calc = Calculator()
    print("Bem-vindo à Calculadora!")
    while True:
        print("\nEscolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Raiz Quadrada")
        print("7. Valor Absoluto")
        print("8. Sair")
        opcao = input("Digite o número da operação: ")

        if opcao == '8':
            print("Saindo...")
            break

        if opcao in ['1', '2', '3', '4', '5']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        elif opcao in ['6', '7']:
            a = float(input("Digite o número: "))

        if opcao == '1':
            resultado = calc.add(a, b)
            print(f"Resultado: {resultado}")
        elif opcao == '2':
            resultado = calc.subtract(a, b)
            print(f"Resultado: {resultado}")
        elif opcao == '3':
            resultado = calc.multiply(a, b)
            print(f"Resultado: {resultado}")
        elif opcao == '4':
            try:
                resultado = calc.divide(a, b)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == '5':
            resultado = calc.power(a, b)
            print(f"Resultado: {resultado}")
        elif opcao == '6':
            try:
                resultado = calc.sqrt(a)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == '7':
            resultado = calc.absolute(a)
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")