from Individuo import Individuo
import math
from random import random
from RepresentacaoNumerica import Conversor

class Geracao:
    TAMANHO = 30
    TAXA_CROSSOVER = 0.7
    TAXA_MUTACAO = 0.01

    def __init__(self, geracao_passada=None):
        self.individuos = []
        if geracao_passada == None:
            for i in range(self.TAMANHO):
                self.individuos.append(Individuo())
        else:
            self.elite = []
            self.selecao(geracao_passada)
            qnt_cortes = Conversor.NUM_BITS
            pai_1 = self.elite[0]
            pai_2 = self.elite[1]
            for pos_corte in range(1, qnt_cortes):
                filho_1, filho_2 = self.crossover(pai_1, pai_2, pos_corte)
                self.individuos.append(filho_1)
                self.individuos.append(filho_2)
            self.repopular()
            self.mutacao()

    def selecao(self, geracao_passada):
        individuos = geracao_passada.individuos
        tamanho = len(individuos)
        meio = tamanho // 2
        grupo1 = individuos[:meio]
        grupo2 = individuos[meio:]
        self.elite = []
        self.elite.append(self.melhor_individuo(grupo1))
        self.elite.append(self.melhor_individuo(grupo2))

    def melhor_individuo(self, lista):
        melhor_valor = -math.inf
        melhor_individuo = None
        for individuo in lista:
            fx = individuo.calcular_fx()
            if fx > melhor_valor:
                melhor_valor = fx
                melhor_individuo = individuo
        return melhor_individuo

    def crossover(self, pai_1, pai_2, pos_corte):
        if random() < self.TAXA_CROSSOVER:
            pt1_pai1 = pai_1.genes[:pos_corte]
            pt2_pai1 = pai_1.genes[pos_corte:]
            pt1_pai2 = pai_2.genes[:pos_corte]
            pt2_pai2 = pai_2.genes[pos_corte:]
            #
            filho_1 = Individuo()
            filho_1.genes = pt1_pai1 + pt2_pai2
            filho_1.auto_correcao()
            #
            filho_2 = Individuo()
            filho_2.genes = pt1_pai2 + pt2_pai1
            filho_2.auto_correcao()
        else:
            filho_1 = pai_1.clonar()
            filho_2 = pai_2.clonar()
        return filho_1, filho_2

    def repopular(self):
        nova_lista_individuos = []
        #
        for individuo in self.elite:
            for i in range(2):
                nova_lista_individuos.append(individuo.clonar())
        #
        for individuo in self.individuos:
            nova_lista_individuos.append(individuo.clonar())
        self.individuos = nova_lista_individuos

    def mutacao(self):
        for individuo in self.individuos:
            individuo.sofrer_mutacao(self.TAXA_MUTACAO)
            individuo.auto_correcao()

    def __str__(self):
        representacao = ""
        for individuo in self.individuos:
            representacao += "x = "+str(individuo.valor)
            representacao += "\n"
        representacao += "\n"
        return representacao
