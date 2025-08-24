class Calculadora:
    def _init_(self):
        self.num1 = 0
        self.num2 = 0

    def ler_numeros(self):
        self.num1 = float(input('Digite o num1: '))
        self.num2 = float(input('Digite o num2: '))

    def soma(self):
        self.ler_numeros()
        resultado = self.num1 + self.num2
        self.exibir_resultado(resultado, "soma")

    def subtracao(self):
        self.ler_numeros()
        resultado = self.num1 - self.num2
        self.exibir_resultado(resultado, "subtração")

    def multiplicacao(self):
        self.ler_numeros()
        resultado = self.num1 * self.num2
        self.exibir_resultado(resultado, "multiplicação")

    def divisao(self):
        self.ler_numeros()
        if self.num2 == 0:
            print("Não é possível dividir por zero.")
            return
        resultado = self.num1 / self.num2
        self.exibir_resultado(resultado, "divisão")

    def exibir_resultado(self, resultado, operacao):
        if resultado == 0:
            print(f"Resultado da {operacao} ({resultado}) é inválido.")
        else:
            print(f"Resultado da {operacao}: {resultado}")

calc = Calculadora()
escolha = input("Escolha uma função: soma, subtracao, multiplicacao ou divisao: ").lower()

match escolha:
    case "soma":
        calc.soma()
    case "subtracao":
        calc.subtracao()
    case "multiplicacao":
        calc.multiplicacao()
    case "divisao":
        calc.divisao()
