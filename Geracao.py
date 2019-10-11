from Individuo import Individuo
import math

class Geracao:
    TAMANHO = 30

    def __init__(self, geracao_passada=None):
        if geracao_passada == None:
            self.individuos = []
            for i in range(self.TAMANHO):
                self.individuos.append(Individuo())
        else:
            self.selecionar(geracao_passada)
#            self.crossover()
#            self.mutacao()

    def selecionar(self, geracao_passada):
        individuos = geracao_passada.individuos
        tamanho = len(individuos)
        meio = tamanho // 2
        grupo1 = individuos[0:meio]
        grupo2 = individuos[meio:tamanho]
        self.elite = []
        self.elite.append(self.melhor_individuo(grupo1))
        self.elite.append(self.melhor_individuo(grupo2))
        for individuo in self.elite:
            print(individuo)

    def melhor_individuo(self, lista):
        melhor_valor = -math.inf
        melhor_individuo = None
        for individuo in lista:
            fx = self.calcular_fx(individuo.valor)
            if fx > melhor_valor:
                melhor_valor = fx
                melhor_individuo = individuo
        return melhor_individuo

    def calcular_fx(self, x):
        fx = x**2 -3*x + 4
        return fx

    def __str__(self):
        representacao = ""
        for individuo in self.individuos:
            fx = self.calcular_fx(individuo.valor)
            representacao += str(individuo)+" "+str(fx)
            representacao += "\n"
        representacao += "\n"
        return representacao
