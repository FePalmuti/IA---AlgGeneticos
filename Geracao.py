from Individuo import Individuo
from random import randint
from random import random
import math
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
            self.selecao(geracao_passada)
            pai_1, pai_2 = self.escolher_pais()
            qnt_cortes = Conversor.NUM_BITS
            for pos_corte in range(1, qnt_cortes):
                filho_1, filho_2 = self.crossover(pai_1, pai_2, pos_corte)
                self.individuos.append(filho_1)
                self.individuos.append(filho_2)
            self.mutacao()
        self.individuo_superior = self.melhor_individuo(self.individuos)

    # Selecao por torneio
    # Eh gerada a nova populacao inteira
    def selecao(self, geracao_passada):
        individuos = geracao_passada.individuos
        self.populacao_intermediaria = []
        for i in range(0, self.TAMANHO):
            competidores = []
            for j in range(2):
                numero_aleatorio = randint(0, self.TAMANHO - 1)
                competidores.append(individuos[numero_aleatorio].clonar())
            self.populacao_intermediaria.append(self.melhor_individuo(competidores))

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
        if x == -math.inf:
            return -math.inf
        else:
            fx = x**2 -3*x + 4
            fx = round(fx, 2)
            return fx

    def escolher_pais(self):
        numero_aleatorio = randint(0, self.TAMANHO - 1)
        pai_1 = self.populacao_intermediaria[numero_aleatorio].clonar()
        numero_aleatorio = randint(0, self.TAMANHO - 1)
        pai_2 = self.populacao_intermediaria[numero_aleatorio].clonar()
        return pai_1, pai_2

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

    def mutacao(self):
        for individuo in self.individuos:
            individuo.sofrer_mutacao(self.TAXA_MUTACAO)
            individuo.auto_correcao()

    def __str__(self):
        representacao = ""
        for individuo in self.individuos:
            fx = self.calcular_fx(individuo.valor)
            representacao += str(individuo)+" "+str(fx)
            representacao += "\n"
        representacao += "\n"
        return representacao
