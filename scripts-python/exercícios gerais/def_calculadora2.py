#Construindo métodos, funções e classes para ganhar reaproveitamento de códigos, sem instanciar os objetos.
class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 5))
print(calculadora.subtracao(25, 5))
print(calculadora.multiplicacao(2, 10))
print(calculadora.divisao(100, 2))