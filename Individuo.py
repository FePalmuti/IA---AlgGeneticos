import math
from random import randint
from random import random

class Individuo:
    V_MIN = -10
    V_MAX = 10
    NUM_BITS = 5

    def __init__(self):
        valor = randint(self.V_MIN, self.V_MAX)
        self.valor = valor
        self.genes = []
        if valor > 0:
            self.genes.append(1)
        else:
            self.genes.append(0)
            valor *= -1
        self.genes = self.genes + self.converter_decimal_binario(valor)
        while len(self.genes) < self.NUM_BITS:
            # Injeta um 0 na posicao 1
            self.genes.insert(1, 0)

    def converter_decimal_binario(self, decimal):
        binario = []
        while decimal != 0 and decimal != 1:
            bit = decimal % 2
            binario.insert(0, bit)
            decimal = decimal // 2
        binario.insert(0, decimal)
        return binario

    def auto_correcao(self):
        self.atualizar_valor()
        if self.valor < self.V_MIN or self.valor > self.V_MAX:
            self.valor = -math.inf

    def atualizar_valor(self):
        copia_genes = self.genes.copy()
        if copia_genes.pop(0) == 1:
            sinal = 1
        else:
            sinal = -1
        indice = len(copia_genes) - 1
        valor = 0
        while copia_genes:
            bit = copia_genes.pop(0)
            valor += bit * 2 ** indice
            indice -= 1
        valor *= sinal
        self.valor = valor

    def sofrer_mutacao(self, taxa):
        for indice in range(len(self.genes)):
            if random() < taxa:
                self.genes[indice] = self.swap(self.genes[indice])

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
        return str(self.valor)+" "+str(self.genes)
#
