from random import randint
from random import random
from RepresentacaoNumerica import Conversor
import math

class Individuo:
    V_MIN = -10
    V_MAX = 10

    def __init__(self):
        int_aleatorio = randint(self.V_MIN * 100, self.V_MAX * 100)
        self.valor = int_aleatorio / 100
        self.genes = Conversor.decimal_para_binario(self.valor)

    def auto_correcao(self):
        self.atualizar_valor()
        if self.valor < self.V_MIN or self.valor > self.V_MAX:
            self.valor = -math.inf

    def atualizar_valor(self):
        self.valor = Conversor.binario_para_decimal(self.genes)

    def sofrer_mutacao(self, taxa):
        for indice in range(len(self.genes)):
            if random() < taxa:
                self.genes[indice] = self.swap(self.genes[indice])

    def calcular_fx(self):
        x = self.valor
        if x == -math.inf:
            return -math.inf
        else:
            fx = x**2 -3*x + 4
            fx = round(fx, 2)
            return fx

    def swap(self, gene):
        if gene == 0:
            return 1
        else:
            return 0

    def clonar(self):
        novo_individuo = Individuo()
        novo_individuo.valor = self.valor
        novo_individuo.genes = self.genes.copy()
        return novo_individuo

    def __str__(self):
        return str(self.genes)+"\n"+\
        "x = "+str(self.valor)+"\n"+\
        "f(x) = "+str(self.calcular_fx())



#
