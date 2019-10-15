from Individuo import Individuo
import math
from random import random

class Geracao:
    TAMANHO = 30
    TAXA_CROSSOVER = 0.7

    def __init__(self, geracao_passada=None):
        self.individuos = []
        if geracao_passada == None:
            for i in range(self.TAMANHO):
                self.individuos.append(Individuo())
        else:
            self.selecionar(geracao_passada)
            qnt_cortes = Individuo.NUM_BITS
            pai_1 = self.elite[0]
            pai_2 = self.elite[1]
            for pos_corte in range(1, qnt_cortes):
                filho_1, filho_2 = self.crossover(pai_1, pai_2, pos_corte)
                self.individuos.append(filho_1)
                self.individuos.append(filho_2)
#            self.mutacao()

    def selecionar(self, geracao_passada):
        individuos = geracao_passada.individuos
        tamanho = len(individuos)
        meio = tamanho // 2
        grupo1 = individuos[:meio]
        grupo2 = individuos[meio:]
        self.elite = []
        self.elite.append(self.melhor_individuo(grupo1))
        self.elite.append(self.melhor_individuo(grupo2))
#        print(self.elite[0], self.elite[1])

    def crossover(self, pai_1, pai_2, pos_corte):
        if random() < self.TAXA_CROSSOVER:
            pt1_pai1 = pai_1.genes[:pos_corte]
            pt2_pai1 = pai_1.genes[pos_corte:]
            pt1_pai2 = pai_2.genes[:pos_corte]
            pt2_pai2 = pai_2.genes[pos_corte:]
#            print(pt1_pai1, pt2_pai1, pt1_pai2, pt2_pai2)
            filho_1 = Individuo()
            filho_1.genes = pt1_pai1 + pt2_pai2
            self.corrigir_filho(filho_1)
            filho_2 = Individuo()
            filho_2.genes = pt1_pai2 + pt2_pai1
            self.corrigir_filho(filho_2)
        else:
            filho_1 = pai_1.clonar()
            filho_2 = pai_2.clonar()
        return filho_1, filho_2

    def corrigir_filho(self, filho):
        filho.atualizar_valor()
        if filho.valor < filho.V_MIN or filho.valor > filho.V_MAX:
            filho.valor = -math.inf

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
