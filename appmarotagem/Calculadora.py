class Calculadora:
    def __init__(self, valor1, valor2, tipo):
        self.valor1 = valor1
        self.valor2 = valor2
        self.tipo = tipo

    def calcular(self):
        if self.tipo == 'A':
            print("O resultado é:", self.valor1 + self.valor2)
        elif self.tipo == 'S':
            print("O resultado é:", self.valor1 - self.valor2)
        elif self.tipo == 'D':
            if self.valor1 == 0 or self.valor2 == 0:
                    print("Impossivel realizar essa divisão")
            else:
                    print("O resultado é:", self.valor1 / self.valor2)
        elif self.tipo == 'M':
            print("O resultado é:", self.valor1 * self.valor2)